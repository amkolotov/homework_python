# скрипт для расчет заработной платы

from sys import argv

def salary(hours, pay_hour, bonus):
    salary = int(hours) * int(pay_hour) + int(bonus)
    return 'Заработная плата равна: ', salary

script_name, hours, pay_hour, bonus = argv

print(salary(hours, pay_hour, bonus))


