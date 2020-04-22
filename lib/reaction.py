import louie
import re
# from lib.store import Store

# class Reactions(store):
# 	def __init__(self):
#         super().__init__()
#         self.notifications = {
#                 "gametime.update": self.update
#             }

class Reaction(object):
	key = ""
	regexes = []
	parser = None

	def __init__(self, key, regex, parser=None):
		self.key = key
		self.regex = regex

		if parser is not None:
			self.parser = parser
		else:
			self.parser = self.default_parser

	def search(self, text):
		match = None
		for r in self.regex:
			try:
				match = re.search(r, text)
			except TypeError:
				pass
			
			if match is not None:
				self.send(match)
				break

	def default_parser(self, match):
		return match

	def send(self, match):
		louie.send(data=self.parser(match), signal=self.key)
