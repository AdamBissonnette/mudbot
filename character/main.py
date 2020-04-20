import louie
from lib.thread import Thread
from character.status import Status
from character.inventory import Inventory

#stores the stores, watches for updates louie notifications and performs updates
class Character(object):
	stores = []
	info = {}  # xp, stats, profficiencies, race, class
	inventory = {}  # equipment, inventory
	status = {}  # hp, mp, resting, hunting, active buffs, debuffs, cooldowns
	mobs = {}  # mobs in the current area
	targets = {}  # mobs being hunted
	area = {}  # current area and exits

	def __init__(self):
		super().__init__()
		self.stores = [Status(), Inventory()]
