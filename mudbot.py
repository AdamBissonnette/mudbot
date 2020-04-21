import louie
import sys
import time
from lib.thread import Thread
from lib.telnet import Telnet
from character.main import Character

class MudBot():
	character = {}
	telnet = {}
	stores = []

	def __init__(self):
		super().__init__()
		#instantiate everything
		self.character = Character()
		self.telnet = Telnet('mud.landsofstone.org', 4801)
		self.stores += self.character.stores
		self.stores.append(self.telnet)
		self.setup_stores()
		self.telnet.start()
	
	def setup_stores(self):
		for store in self.stores:
			for key, callback in store.notifications.items():
				if callable(callback):
					louie.connect(callback, signal=key)
				else:
					print("{} function is not callable".format(key))

class UserInput(Thread):
	def __init__(self):
		super().__init__()

	def do_action(self):
		text = input()
		
		louie.send(text=text, signal=Telnet.signal_write)

		if text == "!exit":
			louie.send(signal="mudbot.killall")

if __name__ == '__main__':
	M = MudBot()
	I = UserInput()
	I.start()
