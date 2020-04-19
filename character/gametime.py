from lib.store import Store

class GameTime(Store):
	gametime_update = "gametime.update"
	gametime = ""

	def __init__(self):
		super().__init__()
		self.notifications = {
			GameTime.gametime_update: self.update
		}

	def update(self, data):
		print("time updated {}".format(data))
		self.set("gametime", data)