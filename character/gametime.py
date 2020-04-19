from lib.store import Store

class GameTime(Store):
	signal_update = "gametime.update"
	gametime = ""

	def __init__(self):
		super().__init__()
		self.notifications = {
			GameTime.signal_update: self.update
		}

	def update(self, data):
		print("time updated {}".format(data))
		self.set("gametime", data)