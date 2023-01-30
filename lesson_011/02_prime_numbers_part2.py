# -*- coding: utf-8 -*-
def is_not_prime(n) -> bool:
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return False if n in prime_numbers else True

# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    for this_number in range(2, n + 1):
        for prime in prime_numbers:
            if this_number % prime == 0:
                break
        else:
            prime_numbers.append(this_number)
    yield prime_numbers
     # TODO здесь ваш код
#
#
# for number in prime_numbers_generator(n=10000):
#     print(number)