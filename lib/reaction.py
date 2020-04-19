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

        if parser is not None:
            self.parser = parser
        else:
            self.parser = self.default_parser

    def default_parser(self, match):
        return match

    def send(self, match):
        louie.send(data=self.parser(match), signal=self.key)
