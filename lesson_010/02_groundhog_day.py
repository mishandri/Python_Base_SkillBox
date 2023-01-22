# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def one_day():
    carma = randint(1, 7)
    end_day = randint(1, 13)
    if end_day == 1:
        raise IamGodError('Почувствовал себя Богом')
    elif end_day == 2:
        raise DrunkError('Напился до потери пульса')
    elif end_day == 3:
        raise CarCrashError('Погиб в автокатастрофе')
    elif end_day == 4:
        raise GluttonyError('Лопнул живот от обжорства')
    elif end_day == 5:
        raise DepressionError('Умер от депрессии')
    elif end_day == 6:
        raise SuicideError('Решил закончить это всё')
    else:
        return carma

ENLIGHTENMENT_CARMA_LEVEL = 0
day = 0

file_log = '02_log.txt'

while ENLIGHTENMENT_CARMA_LEVEL <= 777:
    day += 1
    try:
        carma = one_day()
        ENLIGHTENMENT_CARMA_LEVEL += carma
        with open(file_log, 'a', encoding='utf8') as file:
            file.write(f'День {day}. КАРМА = {ENLIGHTENMENT_CARMA_LEVEL}\n')
    except Exception as exc:
        ENLIGHTENMENT_CARMA_LEVEL -= 1
        with open(file_log, 'a', encoding='utf8') as file:
            file.write(f'День {day}. {exc}. КАРМА = {ENLIGHTENMENT_CARMA_LEVEL}\n')
else:
    print('Наконец-то этот день закончился!')

#

# TODO здесь ваш код

# https://goo.gl/JnsDqu
