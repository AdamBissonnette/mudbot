from lib.store import Store

class Inventory(Store):
	inventory_youhave = "inventory.you_have"

	def __init__(self):
		super().__init__()
		self.notifications = {
				Inventory.inventory_youhave: self.you_have
		}

	def you_have(self, data):
		print("inventory updated {}".format(data))
