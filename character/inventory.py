from lib.store import Store

class Inventory(Store):
	signal_youhave = "inventory.you_have"
	signal_wontbuy = "inventory.wont_buy"

	def __init__(self):
		super().__init__()
		self.notifications = {
				Inventory.signal_youhave: self.you_have,
				Inventory.signal_wontbuy: self.wont_buy
		}

	def you_have(self, data):
		print("inventory updated {}".format(data))

	def wont_buy(self):
		print("inventory updated {}".format(data))
