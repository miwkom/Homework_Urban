class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


h1 = Building(2, 'Cottage')
h2 = Building(1, 'Log hut')
h3 = Building(2, 'Cottage')

print(h1 == h2)
print(h1 == h3)