# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json

dict_firm = {}
sum_prof = 0
num = 0
with open('5.7.txt') as f:
    for line in f:
        firm = line.split()
        profit = int(firm[2]) - int(firm[3])
        dict_firm[firm[0]] = profit
        if profit > 0:
            sum_prof += profit
            num += 1

av_prof = sum_prof // num

aver = {'average_profit': av_prof}

res_list = [dict_firm, aver]

print (res_list)

with open('5.7.json', 'w') as f:
    json.dump(res_list, f)



