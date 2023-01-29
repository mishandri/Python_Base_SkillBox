# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def polygon(angle=0, length=200, width=3):
        for _ in range(n):
            v = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
            v.draw()
            point = v.end_point
            angle += (360 + n - 2) / n


draw_triangle = get_polygon(n=3)

draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)


sd.pause()
