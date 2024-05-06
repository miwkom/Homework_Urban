def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(1, 6, 9)
print_params('a', 'b', 'c')
print_params(True, False, True)
print_params(b=25)
print_params(c=[1, 2, 3])
print()
values_list = [False, 20, 'Привет']
values_dict = {'a': 'Пока', 'b': True, 'c': 38}

print_params(*values_list)
print_params(**values_dict)
print()
values_list_2 = [10, 20]

print_params(*values_list_2, 42)
