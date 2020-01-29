class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number > other.number:
            return Cell(self.number - other.number)
        else:
            print('Разность должна быть больше нуля')
            return Cell(0)

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, count):
        if self.number < count * 2 + 2:
            return '**\\n\\n'
        else:
            return '**\\n\\n' + '*' * (self.number - 12)

cell_1 = Cell(27)
cell_2 = Cell(12)
cell_3 = cell_1 - cell_2
print (cell_3.number)

print (cell_3.make_order(5))
