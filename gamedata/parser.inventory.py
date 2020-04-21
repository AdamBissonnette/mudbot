class Item(object):
    def __init__(self):
        pass

    @staticmethod
    def parse(match):
        return Item()
    
    @staticmethod
    def parse_list(match):
        return [Item()]