def is_prime(func):
    def wrapper(*args):
        num = func(*args)
        k = 0
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                k = k + 1
        if k <= 0:
            print("Простое")
        else:
            print("Составное")
        return num

    return wrapper


@is_prime
def sum_three(*numbers):
    return sum(numbers)


result = sum_three(2, 3, 6)
print(result)
