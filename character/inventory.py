from lib.store import Store

class Inventory(Store):
	signal_youhave = "inventory.you_have"
	signal_wontbuy = "inventory.seller_wont_buy"
	signal_itemsold = "inventory.item_sold"
	signal_itemdropped = "inventory.item_dropped"
	signal_itemdestroyed = "inventory.item_destroyed"
	signal_itemnotempty = "inventory.item_not_empty" #cant drop
	signal_wearitems = "inventory.wear_items"
	signal_nothingtowear = "inventory.nothing_to_wear"
	signal_yougetitems = "inventory.you_get_items"
	signal_removeitems = "inventory.remove_items"

	def __init__(self):
		super().__init__()
		self.notifications = {
				Inventory.signal_youhave: self.you_have,
				Inventory.signal_wontbuy: self.wont_buy
		}

	def you_have(self, data):
		print("inventory updated {}".format(data))

	def wont_buy(self):
		print("wont buy noticed")
