import louie
import sys
import time
from lib.thread import Thread
from character.main import Character

class MudBot():
	character = {}
	def __init__(self):
		super().__init__()
		#instantiate everything
		self.character = Character()

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
