# coding=utf-8
# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

lines = 0
with open('5.2.txt') as f:
    for line in f:
        num = len(line.split())
        lines += 1
        print ('Строка {} содержит {} слов'.format(lines, num))

    print ('В файле всего {} строк'.format(lines))