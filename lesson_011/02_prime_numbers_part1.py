# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых объектов,
# который выдает последовательность простых чисел до n.
#
# Распечатать все простые числа до 10000 в столбик


def is_not_prime(n) -> bool:
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return False if n in prime_numbers else True


class PrimeNumbers:

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        # обнуляем счетчик перед циклом
        self.i = 1
        # возвращаем ссылку на себя - я буду итератором!
        return self

    def __call__(self, n):
        prime_numbers = []
        for this_number in range(2, n + 1):
            for prime in prime_numbers:
                if this_number % prime == 0:
                    break
            else:
                prime_numbers.append(this_number)
        return prime_numbers[-1]

    def __next__(self):
        # а этот метод возвращает значения по требованию python
        a = self.i + 1
        while is_not_prime(a):
            a += 1
        self.i = a
        if self.i <= self.n:
            return self.__call__(self.i)
        raise StopIteration()  # признак того, что больше возвращать нечего


# prime_number_iterator = PrimeNumbers(n=10000)
prime_number_iterator = PrimeNumbers(n=100)
print(list(prime_number_iterator))
for number in prime_number_iterator:
    print(number)
