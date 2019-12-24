# структура данных "Товары"

my_list = []
i = 0
while True:
    i += 1
    dict_i = {}
    dict_i['название'] = input('Введите название товара: ')
    dict_i['цена'] = int(input('Введите цену товара: '))
    dict_i['количество'] = int(input('Введите количество товара: '))
    dict_i['ед'] = input('Введите единицы измерения товара: ')
    my_list.append((i, dict_i))
    
    q = input('Нажмите "q" для выхода, другую для продолжения: ')
    if q == 'q': break
    
print(my_list)

name = []
price = []
quantity = []
units = []
for i in my_list:
    name.append(i[1]['название'])
    price.append(i[1]['цена'])
    quantity.append(i[1]['количество'])
    units.append(i[1]['ед'])

my_dict = {'название': name,
           'цена': price,
           'количество': quantity,
           'ед': units}

print(my_dict)


