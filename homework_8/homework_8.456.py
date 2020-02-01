# проект Склад оргтехники

class StoreHouse:
    @classmethod
    def __init__(cls):
        cls.store = {}

class OfficeEquipment:
    def __init__(self, count):
        self.count = count

class Printer(OfficeEquipment):
    def __init__(self, count):
        super().__init__(count)
        StoreHouse.store['printer'] = count

    def get(self, count):
        get_count = Check.check(count)
        StoreHouse.store['printer'] += get_count

    def send(self, count):
        send_count = Check.check(count)
        StoreHouse.store['printer'] -= send_count

class Scanner(OfficeEquipment):
    def __init__(self, count):
        super().__init__(count)
        StoreHouse.store['scaner'] = count

    def get(self, count):
        get_count = Check.check(count)
        StoreHouse.store['scaner'] += get_count

    def send(self, count):
        send_count = Check.check(count)
        StoreHouse.store['scaner'] -= send_count

class Xerox(OfficeEquipment):
    def __init__(self, count):
        super().__init__(count)
        StoreHouse.store['xerox'] = count

    def get(self, count):
        get_count = Check.check(count)
        StoreHouse.store['xerox'] += get_count

    def send(self, count):
        send_count = Check.check(count)
        StoreHouse.store['xerox'] -= send_count

class OwnEx(Exception):
    def __init__(self, text):
        self.text = text


class Check:
    @staticmethod
    def check(count):
        check = str(count)
        if not check.isdigit():
            print ('Необходимо вводить только числа, операция не выполнена')
            return 0
        else:
            return count

StoreHouse()

printer = Printer(10)
xerox = Xerox(5)
scanner = Scanner(15)
print (StoreHouse.store)

printer.get('qwe')
xerox.get(3)
scanner.send(2)

print (StoreHouse.store)
