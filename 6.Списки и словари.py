my_list = ['Яблоко', 'Апельсин', 'Банан', 'Киви', 'Груша', 'Кокос']
print('Лист:', my_list)
print('Первый элемент:', my_list[0])
print('Последний элемент:', my_list[-1])
print('Подсписок:', my_list[2:5])
my_list[2] = 'Арбуз'
print('Модифицированный лист:', my_list)

my_dict = {'Яблоко': 'Apple', 'Апельсин': 'Orange', 'Банан': 'Banana',
           'Киви': 'Qiwi', 'Груша': 'Pear', 'Кокос': 'Coconut'}
print('Словарь:', my_dict)
print('Перевод:', my_dict['Яблоко'])
my_dict.update({'Слива': 'Plum'})
print('Модифицированный cловарь:', my_dict)
