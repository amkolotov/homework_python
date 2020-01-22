# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников

count = []
surname = []
with open('5.3.txt') as f:
    for line in f:
        list_emp = line.split()
        if int(list_emp[1]) < 20000:
            surname.append(list_emp[0])
        count.append(int(list_emp[1]))
    average = sum(count) // len(count)
    print ('Оклад менее 20000 у следующих сотрудников ', [sur for sur in surname])
    print ('Средняя доход сотрудников: ', average)

