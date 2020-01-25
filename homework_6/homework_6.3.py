class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income

class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self.income['wage'] + self.income['bonus']

ivan = Position('Ivan', 'Ivanov', 'driver', {'wage': 10000, 'bonus': 5000})
petya = Position('Petr', 'Sidorov', 'manager', {'wage': 15000, 'bonus': 7000})

print (ivan.get_full_name())
print (petya.get_full_name())

print (ivan.get_total_income())
print (petya.get_total_income())

print (ivan.position)
print (petya.position)



