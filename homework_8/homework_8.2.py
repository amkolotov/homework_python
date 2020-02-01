# coding=utf-8
class OwnEx(Exception):
    def __init__(self, text):
        self.text = text

while True:
    x = int(input('Введите делимое: '))

    try:
        y = int(input('Введите делитель: '))
        if y == 0:
            raise OwnEx('Делить на ноль нельзя')

    except OwnEx as ex:
        print(ex)

    else:
        print ('Результат деления:', x / y)
        break