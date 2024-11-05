def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        if res > 1:
            for n in range(2, res):
                if res % n == 0:
                    return f'Составное'
            else:
                return f'Простое'
        else:
            return f'Не является ни простым, ни составным числом'
    return wrapper


@is_prime
def sum_three(*numbers):
    total = sum(numbers[:3])
    return total


result = sum_three(2, 3, 6)
print(result)
