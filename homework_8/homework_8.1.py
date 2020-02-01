# coding=utf-8
class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def my_number(cls, data):
        my_num = list(map(int, data.split('-')))
        cls.valid(my_num)

    @staticmethod
    def valid(my_num):
        for i in range(3):
            if i == 0 and not 1 <= my_num[i] <= 31:
                print ('Некорректное число месяца')

            elif i == 1 and not 1 <= my_num[i] <= 12:
                print ('Некоректный месяц')

            elif i == 2 and not 1980 <= my_num[i] <= 2020:
                print ('Некорректный год')

print (Data.my_number('10-12-2021'))