class Prompt(object):
    hp = 0
    mp = 0

    def __init__(self, hp, mp):
        self.hp = hp
        self.mp = mp

    @staticmethod
    def parse(match):
        return Prompt(int(match.group(1)), int(match.group(2)))
