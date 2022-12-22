# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника +
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg
def point(x=0, y=0):
    return sd.get_point(x, y)


def triangle(x=0, y=0, angle=0, length=200, width=3):
    """
    Рисует равносторонний треугольник
    """
    start_point = point(x, y)
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=width)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=width)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=width)
    v1.draw()
    v2.draw()
    v3.draw()


def square(x=0, y=0, angle=0, length=200, width=3):
    """
    Рисует квадрат
    """
    start_point = point(x, y)
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=width)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=width)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=width)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=width)
    v1.draw()
    v2.draw()
    v3.draw()
    v4.draw()


def pentagon(x=0, y=0, angle=0, length=200, width=3):
    """
    Рисует пятиугольник
    """
    start_point = point(x, y)
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=width)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=width)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=width)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=width)
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length, width=width)
    v1.draw()
    v2.draw()
    v3.draw()
    v4.draw()
    v5.draw()


def hexagon(x=0, y=0, angle=0, length=200, width=3):
    """
    Рисует пятиугольник
    """
    start_point = point(x, y)
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=width)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=width)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=width)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=width)
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=width)
    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length, width=width)
    v1.draw()
    v2.draw()
    v3.draw()
    v4.draw()
    v5.draw()
    v6.draw()


def polygon(x=0, y=0, sides=3, angle=0, length=200, width=3):
    start_point = point(x, y)
    for _ in range(sides):
        v = sd.get_vector(start_point=start_point, angle=angle, length=length, width=width)
        v.draw()
        start_point = v.end_point
        angle += (360 + sides-2)/sides


# TODO здесь ваш код
# triangle(10, 10, 20, 100, 3)
# square(100, 100, 45, 100, 3)
# pentagon(200, 200, 45, 100, 3)
# hexagon(300, 300, 45, 100, 3)
polygon(300, 300, 3, 45, 500, 3)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы, что бы внести изменения в код? Выгода на лицо
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копипасту!


sd.pause()
