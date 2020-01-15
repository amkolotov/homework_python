# функция деления двух чисел

def division():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    try:
        return round((a / b), 2)
    except ZeroDivisionError:
        return ('Деление на ноль')

print(division())
