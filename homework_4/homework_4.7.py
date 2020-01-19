# факториал с помощью функции с ключевым словом yield

def fibo_gen():
    for n in range(1, 16):
        yield n

fact = 1
for el in fibo_gen():
    fact *= el
    print (fact)