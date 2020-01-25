class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_police

    def go(self):
        print('Машина', self.name, 'поехала')

    def stop(self):
        print('Машина', self.name, 'остановилась')

    def turn(self, direction):
        print('Машина', self.name, 'повернула', direction)

    def show_speed(self):
        print(self.name, 'движется со скоростью', self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print ('Превышение скорости')
        else:
            print(self.name, 'движется со скоростью', self.speed)

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print ('Превышение скорости')
        else:
            print(self.name, 'движется со скоростью', self.speed)

class PoliceCar(Car):
    pass




car = Car(50, 'green', 'Lada')
car.go()
car.stop()
car.show_speed()
car.turn('направо')
print(car.name)

town_car = TownCar(80, 'red', 'Reno')
town_car.go()
town_car.show_speed()
print(town_car.color)
print(town_car.is_polise)

sport_car = SportCar(100, 'blue', 'Honda')
sport_car.go()
sport_car.stop()
sport_car.show_speed()
sport_car.turn('направо')