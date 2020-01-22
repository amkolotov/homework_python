# coding=utf-8
# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка

with open('5.1.txt', 'w') as f:
    str_list = []
    while True:
        str_in = (input('Введите строку, для записи строк в файл 5.1.txt введите пустую строку: '))
        if not str_in: break
        str_in += '\n'
        str_list.append(str_in)
    f.writelines(str_list)

print ('Строки записаны в файл 5.1.txt')