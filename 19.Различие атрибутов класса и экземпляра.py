class Building:
    total = 0

    def __init__(self, name):
        Building.total += 1
        self.name = name

    def __str__(self):
        return f"{self.name}"


for i in range(40):
    a = Building('House')
    print(a.__str__())

print(Building.total)
