# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('5.5.txt', 'w') as f:
    f.write('5 3 7 4 2 7 89')

with open('5.5.txt') as f:
    str_num = f.read()
    print(sum([int(n) for n in str_num.split()]))