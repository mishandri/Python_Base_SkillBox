# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число простое:

numbers = [727, 8, 10, 3, 7, 11, 557, 555]

def is_prime(n):
    k = 0
    for number in range(2,  n // 2 + 1):
        if n % number == 0:
            k += 1
    return True if k <=0 else False

filter_numbers = filter(is_prime, numbers)
print(list(filter_numbers))