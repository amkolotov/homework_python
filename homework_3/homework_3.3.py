# функция нахождения двух наибольших аргументов

def max_numbers(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return numbers[-1], numbers[-2]

print(max_numbers(1, 2, 3))