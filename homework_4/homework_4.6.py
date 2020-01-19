import itertools

# бесконечный итератор, генерирующий целые числа, начиная с указанного

for el in itertools.count(25):
    if el > 50: break
    print (el)

# бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее

n = 0
for el in itertools.cycle('Hello'):
    if n > 20: break
    print (el)
    n += 1