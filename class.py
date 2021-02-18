class Car:
    def __init__(self, size = 'medium', color = 'grey', seat = 4, engine = 1.6):
        self.size = size
        self.color = color
        self.seat = seat
        self.engine = engine

    def parametr(self):
        a = 'Размер - ' + self.size + ', цвет - ' + self.color + ', мест - ' + str(self.seat) + ', объем двигателя - ' + str(self.engine)
        print(a)

bmw = Car('small', 'blue', 2, 2.4)
bmw.parametr()
print(bmw.seat)