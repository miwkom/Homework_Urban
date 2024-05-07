def test(n, *args, txt="Тескт"):
    print(n, args, txt)


test(1, 1, 1, 2, 2)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))
