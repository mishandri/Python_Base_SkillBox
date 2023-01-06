# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.

class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if type(other) is Air:
            return Storm()
        elif type(other) is Fire:
            return Steam()
        elif type(other) is Water:
            return Water()
        elif type(other) is Earth:
            return Dirt()
        else:
            return None


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if type(other) is Water:
            return Storm()
        elif type(other) is Fire:
            return Flash()
        elif type(other) is Earth:
            return Dust()
        elif type(other) is Air:
            return Air()
        else:
            return None


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if type(other) is Water:
            return Steam()
        elif type(other) is Air:
            return Flash()
        elif type(other) is Earth:
            return Lava()
        elif type(other) is Fire:
            return Fire()
        else:
            return None


class Earth:
    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if type(other) is Fire:
            return Lava()
        elif type(other) is Air:
            return Dust()
        elif type(other) is Water:
            return Dirt()
        else:
            return None


class Storm:
    def __str__(self):
        return 'Шторм'

    def __add__(self, other):
        if type(other) is Storm:
            return Storm()
        else:
            return None


class Steam:
    def __str__(self):
        return 'Пар'

    def __add__(self, other):
        if type(other) is Steam:
            return Steam()
        else:
            return None


class Dirt:
    def __str__(self):
        return 'Грязь'

    def __add__(self, other):
        if type(other) is Dirt:
            return Dirt()
        else:
            return None


class Flash:
    def __str__(self):
        return 'Молния'

    def __add__(self, other):
        if type(other) is Flash:
            return Flash()
        else:
            return None


class Dust:
    def __str__(self):
        return 'Пыль'

    def __add__(self, other):
        if type(other) is Dust:
            return Dust()
        else:
            return None


class Lava:
    def __str__(self):
        return 'Лава'

    def __add__(self, other):
        if type(other) is Lava:
            return Lava()
        else:
            return None


# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

elements = [Water(), Air(), Fire(), Earth(), Storm(), Steam(), Dirt(), Dust(), Lava()]
for element in elements:
    for other_element in elements:
        print(element, '+', other_element, '=', element + other_element)
# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())
water = Water()
air = Air()
print(type(Air() + Water()))
print(type(air + water))
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
