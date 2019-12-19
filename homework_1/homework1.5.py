# определение прибыли фирмы

revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))

profit = revenue - costs

if profit > 0:
    print('Прибыль вашей фирмы составила:', profit)
    
    profitability = round(profit / revenue * 100, 2)
    print(f'Рентабельность выручки составила {profitability}')
    
    number_worker = int(input('Введите количество работников фирмы:'))
    profit_worker = round(profit / number_worker, 2)
    print('Прибыль фирмы на одного работника составила', profit_worker)
    
elif profit == 0:
    print('У вас нет ни прибыли ни убытков')
    
else:
    print('Убытки вашей фирмы составили: ', abs(profit))