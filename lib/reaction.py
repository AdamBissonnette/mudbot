import louie
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
        self.parser = parser
    
    def send(self, text):
        louie.send(data=self.parser(text), signal=self.key)
