import sys
import telnetlib3
import asyncio
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
	signal_read = "telnet.read"
	signal_closed = "telnet.closed"
	signal_crashed = "telnet.crashed"

	server = ""
	port = 0
	server_timeout = 299
	select_timeout = 2
	connected = False
	stopping = False

	loop = None
	tn = None
	reader = None
	writer = None

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
		self.loop = asyncio.new_event_loop()

	def set_timer(self):
		self.timer = time.time() + self.server_timeout

	def stop(self):
		self.close()

	def close(self):
		self.stopping = True
		louie.send(signal=Telnet.signal_closed)

	def write(self, text):
		self.writer.write(text + "\n")
		louie.send(data=text, signal=Telnet.signal_write_sent)

	@asyncio.coroutine
	def shell(self, reader, writer):
		while not self.stopping:
			outp = yield from reader.read(1024)
			sys.stdout.write(outp)
			sys.stdout.flush()
			if 'Goodbye! Come back soon.' in outp:
				self.stopping = True

		return

	def do_action(self):
		if not self.connected:
			asyncio.set_event_loop(self.loop)
			coro = telnetlib3.open_connection(self.server, self.port, shell=self.shell)
			self.reader, self.writer = self.loop.run_until_complete(coro)
			self.loop.run_until_complete(self.writer.protocol.waiter_closed)
			self.loop.stop()
			# Find all running tasks:
			pending = asyncio.Task.all_tasks()

			# Run loop until tasks done:
			self.loop.run_until_complete(asyncio.gather(*pending))
			print("shutdown complete")
