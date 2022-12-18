#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.
# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
print(my_favorite_movies[:10])
#   последний
print(my_favorite_movies[-15:])
#   второй
print(my_favorite_movies[12:25])
#   второй с конца
print(my_favorite_movies[-22:-17])
