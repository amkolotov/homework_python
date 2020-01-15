# вывод суммы чисел

def my_sum(a):
    return sum([int(n) for n in a])

current = 0
while True:
    a = input('Введите числа через пробел, для выходы добавте "q" :')
    a = a.split()
    if 'q' in a:
        a = a[: a.index('q')]
        current += my_sum(a)
        print('Итоговая сумма равна', current)
        break
    else:
        current += my_sum(a)
        print ('Сумма равна: ', current)

