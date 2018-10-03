class Player:
    def __init__(self, name, hand=None, money=1000.0, sb='', bb=''):
        self.name = name
        self.hand = hand
        self.money = money
        self.sb = sb
        self.bb = bb

    def display(self):
        if self.sb != '':
            return [self.name, self.hand, self.money, self.sb]
        if self.bb != '':
            return [self.name, self.hand, self.money, self.bb]
        return [self.name, self.hand, self.money]
