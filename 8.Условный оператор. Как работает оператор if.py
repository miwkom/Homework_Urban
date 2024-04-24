x = -8
print('Привет.')
print('x < 0?')
if x < 0:
    print('Меньше нуля')
print('Пока.')
print('Примеры чисел a и b')
a, b = 56, 6
if a > b:
    print('a>b')
if a > b and a > 0:
    print('1.Успех')
if (a > b) and (a > 0 or b < 1000):
    print('2.Успех')
if 5 < b < 10:
    print('3.Успех')
print('Сравнение str и списка')
if '34' > '120':
    print('1.Успех')
if '123' > '12':
    print('2.Успех')
if [1, 2] > [1, 1]:
    print('3.Успех')
print('Сравнение разных типов')
if '6' > 5:
    print('1.Успех')
if [5, 6] > 5:
    print('2.Успех')
if '6' != 5:
    print('3.Успех')
