class Store(object):
	notifications = {}

	def __init__(self):
		pass
	
	def get(self,key):
		return getattr(self, key)

	def set(self, key, value):
		setattr(self, key, value)
	
