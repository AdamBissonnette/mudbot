import sys
import telnetlib
import socket
import time
import louie
import select
from lib.store import Store
from lib.thread import Thread

class Telnet(Thread, Store):
	signal_disconnect = "telnet.disconnect"
	signal_connected = "telnet.connected"
	signal_write = "telnet.write"
	signal_write_sent = "telnet.write_sent"
	signal_closed = "telnet.closed"
	signal_crashed = "telnet.crashed"

	server = ""
	port = 0
	server_timeout = 299
	select_timeout = 2
	connected = False

	tn = None

	def __init__(self, server, port):
		super().__init__()
		self.set_timer()
		self.daemon = True

		self.notifications = {
			Telnet.signal_write: self.write,
			Telnet.kill_signal: self.close
		}

		self.server = server
		self.port = port

		self.notifications = {
			Telnet.signal_write: self.write,
			Telnet.signal_disconnect: self.close
		}

	def set_timer(self):
		self.timer = time.time() + self.server_timeout

	def stop(self):
		super().stop()
		self.close()

	def close(self):
		if self.tn is not None:
			self.tn.close()
		louie.send(signal=Telnet.signal_closed)

	def write(self, text):
		self.set_timer()
		text += '\r'
		try:
			self.tn.write(text.encode('ascii'))
		except socket.error:
			raise socket.error

		louie.send(data=text, signal=Telnet.signal_write_sent)

	def do_action(self):
		if not self.connected:
			try:
				self.tn = telnetlib.Telnet(self.server, self.port, 25)
				self.connected = True
				louie.send(signal=Telnet.signal_connected)
			except socket.error:
				self.connected = False
				time.sleep(5)
		else:
			fragment = ""
			select_out = ([], [], [])
			socket_number = self.tn.get_socket()
			try:
				select_out = select.select([socket_number], [], [], self.select_timeout)
			except ValueError:
				pass
			
			if (select_out != ([], [], []) or socket_number == 1):
				try:
					fragment += self.tn.read_some().decode('ascii', errors='ignore')
					sys.stdout.write(fragment)
				except (EOFError, OSError):
					louie.send(signal=Telnet.signal_crashed)
			else:
				pass

		# The server times out every 5 minutes - I'd prefer it to be 10 minutes,
		# so I send a 'rest' command when we're about to time out.
		# else:
		# 	if self.timer > time.time():
		# 		time.sleep(max(0, self.timer - time.time()))
		# 	self.tn.write('rest\r'.encode('ascii'))
		# 	time.sleep(self.server_timeout)
