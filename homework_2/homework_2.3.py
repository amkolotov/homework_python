# вывод времени года по номеру месяца

num = input('Введите порядковый номер месяца: ')

my_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето',
           'лето', 'лето', 'осень', 'осень', 'осень', 'зима']

print('Данный месяц относится к времени года', my_list[int(num) - 1])

my_dict = {'12': 'зима', '1': 'зима', '2': 'зима',
           '3': 'весна', '4': 'весна', '5': 'весна',
           '6': 'лето', '7':'лето', '8':'лето',
           '9':'осень', '10':'осень', '11':'осень'}

print('Данный месяц относится к времени года', my_dict[num])

