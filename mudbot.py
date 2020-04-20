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
		print(self.stores)
		self.stores.append(self.telnet)
		print(self.stores)
		self.setup_stores()

		# self.telnet.start()
	
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
		print("received {}".format(text))
		if text == "time":
			louie.send(data="time time time", signal="gametime.update")
		if text == "inv":
			louie.send(data="time time time", signal="inventory.you_have")
		if text == "quit":
			louie.send(signal="mudbot.killall")

if __name__ == '__main__':
	M = MudBot()
	I = UserInput()
	I.start()
