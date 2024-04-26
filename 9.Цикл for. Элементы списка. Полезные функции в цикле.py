brand_car = ["BMW", "MB", "LADA", "KIA", "HONDA"]
for i in brand_car:
    print('Я езжу на автомабиле марки ' + i)

cars_count = 0
for j in range(len(brand_car)):
    cars_count += 10
    for i in brand_car:
        print("У меня есть", cars_count, i)
