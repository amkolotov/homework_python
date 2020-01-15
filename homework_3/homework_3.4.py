# возведение числа в степень

def my_func(x, y):
    return x ** y

def my_func2(x, y):
    z = x
    for i in range(1, abs(y)):
        z *= x
    return 1 / z

a = int(input('Введите число: '))
b = int(input('Введите степень для возведения числа: '))

print(my_func(a, b))

print (my_func2(a, b))





