# coding=utf-8
class OwnEx(Exception):
    def __init__(self, text):
        self.text = text

my_list = []

while True:

    n = input('Введите число для добавления в список, для окончания введите "q": ')

    if n == 'q':
        break
    else:
        try:
            if not n.isdigit():
                raise OwnEx('Необходимо вводить только числа')
        except OwnEx as ex:
            print (ex)
        else:
            my_list.append(n)

print('Итоговый список:', my_list)