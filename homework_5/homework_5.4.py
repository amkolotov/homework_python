# coding=utf-8
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_dict = {'1': 'Один', '2':'Два', '3':'Три', '4':'Четыре'}

with open('5.4.1.txt') as f:
    for line in f:
        line = line.split()
        with open('5.4.2.txt', 'a') as t:
            if line[-1] in my_dict:
                string = '{} - {}\n'.format(my_dict[line[-1]], line[-1])
                t.write(string)
