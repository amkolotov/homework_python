class Clothes:
    def __init__(self):
        self.consum = 0
        self.cloth = []

    def add_coat(self, size):
        self.cloth.append(Coat(size))

    def add_suit(self, height):
        self.cloth.append(Suit(height))

    @property
    def total(self):
        return sum([el.cloth for el in self.cloth])

class Coat:
    def __init__(self, size):
        self.cloth = size / 6.5 + 0.5

class Suit:
    def __init__(self, height):
        self.cloth = 2 * height + 0.3

clothes = Clothes()

clothes.add_coat(50)
clothes.add_coat(82)
clothes.add_suit(180)
clothes.add_suit(120)

print (clothes.total)



