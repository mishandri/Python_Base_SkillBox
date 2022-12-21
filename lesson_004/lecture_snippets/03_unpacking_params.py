# -*- coding: utf-8 -*-

# распаковка параметров (аргументов)
def vector_module(x, y, z):
    return (x ** 2 + y ** 2 + z ** 2) ** .5


# распаковка позиционных параметров
some_list = [2, 3, 4]
res = vector_module(*some_list)  # * -- вызов списка позиционных параметров
# x, y, z = some_list
# vector_module(2, 3, 4)
print(res)


# распаковка именованных параметров
some_dict = {'x': 2, 'y': 3, 'z': 4}
res = vector_module(**some_dict)  # ** -- вызов по ключам
# vector_module(x=2, y=3, z=4)
print(res)

# можно совмещать
some_list = [2, 3]
some_dict = dict(z=4)
res = vector_module(*some_list, **some_dict)  # * -- список позиционных параметров, ** -- вызов именованного параметра
# vector_module(2, 3, z=4)

some_list = [3, 4]
res = vector_module(2, *some_list)  # Первый позиционный, а остальные взять из списка позиционных
print(res)

# самый лучший и устойчивый вызов -- именованными параметрами
res = vector_module(x=2, y=3, z=4)
print(res)
