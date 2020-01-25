# Создать класс TrafficLight (светофор)

import time

class TrafficLight:
    def __init__(self):
        self.__color = None
    def running(self):
        __color = 'red'
        print(__color)
        time.sleep(7)
        __color = 'yellow'
        print(__color)
        time.sleep(2)
        __color = 'green'
        print(__color)
        time.sleep(5)

traf = TrafficLight()
traf.running()


