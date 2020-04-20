from lib.store import Store

class Status(Store):
	signal_gametime = "status.gametime"
	signal_prompt = "status.prompt"
	signal_goldreceived = "status.gold_received"
	
	time = ""
	hp = 0
	mp = 0

	def __init__(self):
		super().__init__()
		self.notifications = {
			Status.signal_gametime: self.gametime,
			Status.signal_prompt: self.prompt
		}

	def gametime(self, data):
		print("time updated {}".format(data))
		self.set("gametime", data)

	def prompt(self, data):
		print(data)