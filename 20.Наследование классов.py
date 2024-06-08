class Car:
    price = 1000000

    def horse_powers(self):
        print(200)


class Nissan(Car):
    price = 1200000

    def horse_powers(self):
        print(250)


class Kia(Car):
    price = 800000

    def horse_powers(self):
        print(150)


car1 = Nissan()
car2 = Kia()
print(car1.price)
print(car2.price)
car1.horse_powers()
car2.horse_powers()
