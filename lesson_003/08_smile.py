# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: координата X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
def smile(center_x, center_y):
    """
    Рисует смайлик
    """
    center = sd.get_point(center_x, center_y)
    left = sd.get_point(center_x-50, center_y +50)
    right = sd.get_point(center_x+50, center_y +50)
    smile = sd.get_point(center_x, center_y - 100)
    sd.circle(center, 200)
    sd.circle(left, 10)
    sd.circle(right, 10)
    sd.circle(smile, 10)


smile(300,300)
sd.pause()
