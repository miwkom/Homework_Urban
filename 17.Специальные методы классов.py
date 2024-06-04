class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print("Новое количество этажей:", self.numberOfFloors)


h1 = House()

h1.setNewNumberOfFloors(3)
h1.setNewNumberOfFloors(10)
