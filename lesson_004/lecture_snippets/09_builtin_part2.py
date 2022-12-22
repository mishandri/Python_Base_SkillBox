# -*- coding: utf-8 -*-

profit = [100, 20, 5, 1200, 42, ]

# --- Логические ---

# all() - True если ВСЕ элементы списка/множества True. К каждому элементу применяется bool и and между всеми
all([True, True, True, True, ])   # True
all([1, 0, 1, ])                  # False
all([1, '0', 1, ])                # True
all(['1', True, 1])               # True

# any() - True если ХОТЯ БЫ ОДИН элемент списка True
any([True, False, True, True, ])  # True
any([1, 0, None, ])               # True

# --- Интроспекция ---

# dir() - список всех аттрибутов объекта
dir(profit)
dir([])

# help() - встроенная помощь по функции/объекту
help(profit)
help(print)

# id() - внутренний идентификатор объекта
a = [1, 2, 3]
print(id(a))
b = a
print(id(b))
c = [1, 2, 3]
print(id(c))
print(a == b, a is b, id(a) == id(b))  # is - сравнивает id объектов. True если совпадают
print(a == c, a is c, id(a) == id(c))
print(id(None))
print(id(False))
print(id(True))

# --- Общего назначения ---

# hash() - значение хэша для объекта. Что такое хэш-функции см https://goo.gl/gZLM4o
hash('Кржижановский')   # Число типа int
hash(profit)            # Ошибка, hash можно брать только для неизменяемых объектов

# isinstance() - является ли объект объектом данного класса
isinstance(profit, list)

# type() - тип(КЛАСС) обьекта
type(profit)

# open() - открыть файл на файловой системе
ff = open('lesson_004/lecture_snippets/08_builtin_part1.py', 'r')
for line in ff.readlines():
    print(line, end='')
ff.close()
# будет целый урок по работе с файлами, пока просто ознакомились
