# -*- coding: utf-8 -*-

# Есть множество функций, которые встроены в интерпретатор

# известные нам
# input() - ввод из консоли
# print() - вывод на консоль
# enumerate() - выдать пары (номер элемента, значение) для списков
# range() - выдать последовательность целых чисел

# другие, наиболее употребляемые

# --- Приведение типов ---
int()    # В целое число
float()  # В число с плавающей точкой
bool()   # В True или False
str()    # В строку
list()   # В список
tuple()  # В кортеж
dict()   # В словарь
set()    # Во множество

# Примеры
int('123')       # 123
float(123)       # 123.0
int(123.45)      # 123
float('123')     # 123.0
float('123.45')  # 123.45

bool(123)     # True
bool(0)       # False
bool(123.45)  # True
bool(0.0)     # False
bool('123')   # True
bool('0')     # True
bool('')      # False
bool(None)    # False

str(123)      # '123'
str(123.45)   # '123.45'
str(True)     # 'True'
str(None)     # 'None'

my_tuple = (1, 2, 3, 3, 2, 1)
list(my_tuple)                # [1, 2, 3, 3, 2, 1]
set(my_tuple)                 # {1, 2, 3}

my_dict = {'a': 1, 'b': 2}
list(my_dict)                 # ['a', 'b']
set(my_dict)                  # {'a', 'b'}
bool(my_dict)                 # True если не пустой словарь, False если пустой

dict([('a', 2), ('b', 3), ])  # {'a': 2, 'b': 3}


# --- Числа ---

# abs() - абсолютное значение числа (модуль
abs(1)
abs(-1)

# round() - округление до нужного знака
round(3.1425926, 2)
round(3.1425926, 3)
round(3.1425926, 0)

# --- Cписки ---

profit = [100, 20, 5, 1200, 42, ]


len(profit)        # len() - размер списка
max(profit)        # max() - максимальный элемент (все элементы должны быть сравниваемы)
min(profit)        # min() - минимальный элемент (все элементы должны быть сравниваемы)
sorted(profit)     # sorted() - отсортированный список (новый список)
sum(profit)        # sum() - сумма элементов списка (все элементы должны числами)


# zip() - попарная компоновка элементов двух списков
profit = [100, 20, 5, 1200, 42, ]
days = ['пн', 'вт', 'ср', 'чт', 'пт', ]
res = zip(days, profit, )
list(res)                # [('пн', 100), ('вт', 20), ('ср', 5), ('чт', 1200), ('пт', 42)]
dict(zip(days, profit))  # {'пн': 100, 'вт': 20, 'ср': 5, 'чт': 1200, 'пт': 42}