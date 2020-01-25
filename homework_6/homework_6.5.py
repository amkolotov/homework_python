class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print ('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print ('Запуск отрисовки ручкой')

class Pencil(Stationery):
    def draw(self):
        print ('Запуск отрисовки карандашем')

class Handle(Stationery):
    def draw(self):
        print ('Запуск отрисовки маркером')

stat = Stationery('Канцелярия')
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

print (stat.title)
print (pen.title)
print (pencil.title)
print (handle.title)

stat.draw()
pen.draw()
pencil.draw()
handle.draw()









