# вывод каждого слова введенной строки в отдельной строке с номером

my_str = input('Введите строку: ')

my_list = my_str.split()

for i, n in enumerate(my_list):
    print((i + 1), n[:10])

