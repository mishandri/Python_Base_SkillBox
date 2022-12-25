# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
from random import randint

global game

def generate_number():
    number = []
    while len(number) != 4:
        new_digit = randint(1, 9)
        if str(new_digit) not in number:
            number.append(str(new_digit))

    return number


def print_number(number):
    print("".join(number))


def check_number(number, my_number):
    bulls = 0
    cows = 0
    if my_number == number:
        game_over()
    else:
        for i in range(4):
            if my_number[i] == number[i]:
                bulls += 1
                continue
            elif my_number[i] in number:
                cows += 1
        print("Быки:", bulls, "Коровы:", cows)
    return {'bulls': bulls, 'cows': cows}


def game_over():
    print('Игра окончена, число угадано')

