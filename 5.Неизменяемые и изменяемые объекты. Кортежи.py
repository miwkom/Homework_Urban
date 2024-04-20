immutable_var = (1, 2, 'a', 'b')
# immutable_var[2] = 4
print('Неизменяемые переменные: ', immutable_var)

mutable_list = [1, 2, 'a', 'b']
mutable_list.extend([3, 'c'])
print('Изменяемый лист: ', mutable_list)
