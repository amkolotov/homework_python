# функция вывода данных о пользователе

def user(var_1, var_2, var_3, var_4, var_5, var_6):
    print('Данные пользователя: имя: {}, фамилия: {}, дата рождения: {}, email: {}, номер телефона: {}'.format(var_1, var_2, var_3, var_4, var_5, var_6))


name = input('Введите имя пользователя: ')
surname = input('Введите фамилию пользователя: ')
birth = input('Введите дату рождения пользователя: ')
city = input('Введите город проживания пользователя: ')
email = input('Введите email пользователя: ')
number = input('Введите номер телефона пользователя: ')

user(var_1 = name, var_2 = surname, var_3 = birth, var_4 = city, var_5 = email, var_6 = number)