# определение номера дня, на который спортсмен достигнет указанных результатов

a = int(input('Введите результат спортсмена в первый день: '))
b = int(input('Введите результат, которого необходимо достичь: '))

day = 1

while True:
    if a >= b: break
    a *= 1.1
    day += 1
    
print(f'Указанного результата спортсмен достигнет на {day} день')
    



