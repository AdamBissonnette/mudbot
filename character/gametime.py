from lib.store import Store

class GameTime(Store):
	gametime = ""

	def __init__(self):
		super().__init__()
		self.notifications = {
			"gametime.update": self.update
		}

	def update(self, data):
		print("time updated {}".format(data))
		self.set("gametime", data)