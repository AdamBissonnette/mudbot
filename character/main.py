import louie
from lib.thread import Thread
from character.gametime import GameTime

#stores the stores, watches for updates louie notifications and performs updates
class Character(object):
	stores = []
	gametime = {}  # runtime, #gametime, #realtime
	info = {}  # xp, stats, profficiencies, race, class
	inventory = {}  # equipment, inventory
	status = {}  # hp, mp, resting, hunting, active buffs, debuffs, cooldowns
	mobs = {}  # mobs in the current area
	targets = {}  # mobs being hunted
	area = {}  # current area and exits

	def __init__(self):
		super().__init__()
		self.stores.append(GameTime())
		self.setup_stores()

	def setup_stores(self):
		for store in self.stores:
			for key, callback in store.notifications.items():
				if callable(callback):
					louie.connect(callback, signal=key)
