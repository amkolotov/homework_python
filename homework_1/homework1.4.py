# нахождение самой большой цифры в числе

number = int(input('Введите число: '))
n = 0
while number > 0:
    if number % 10 > n:
        n = number % 10
    number //= 10

print(n)