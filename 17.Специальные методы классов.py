class House:
    def __init__(self, address, number_of_floor):
        self.name = address
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if new_floor > self.number_of_floor:
            print("Такого этажа не существует")
        else:
            for i in range(new_floor):
                print(i + 1)

    def set_new_number_of_floor(self, floor):
        self.number_of_floor = floor


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

print(h1.number_of_floor)
print(h2.number_of_floor)
print()

h1.set_new_number_of_floor(5)
h2.set_new_number_of_floor(10)

print(h1.number_of_floor)
print(h2.number_of_floor)
