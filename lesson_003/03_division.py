# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 179, 37
a_start, b_start = a, b
integer = 0

while a >= b:
    a -= b
    integer += 1

print('Целочисленное деление', a_start, 'на', b_start, 'дает', integer)
