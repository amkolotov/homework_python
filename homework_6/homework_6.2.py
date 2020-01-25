# Реализовать класс Road (дорога)
#  Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.__thick = 0.05
        self.__consumption = 25

    def mass(self):
        self.mass = self._length * self._width * self.__thick * self.__consumption
        return self.mass

m = Road(1000, 10)
print(m.mass())

