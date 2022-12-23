# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def point(x=0, y=0):
    return sd.get_point(x, y)


def polygon(x=0, y=0, sides=3, angle=0, length=200, width=3, color=sd.COLOR_YELLOW):
    start_point = point(x, y)
    for _ in range(sides):
        v = sd.get_vector(start_point=start_point, angle=angle, length=length, width=width)
        v.draw(color=color)
        start_point = v.end_point
        angle += (360 + sides-2)/sides


colors = [sd.COLOR_GREEN, sd.COLOR_YELLOW, sd.COLOR_ORANGE, sd.COLOR_RED, sd.COLOR_BLACK, sd.COLOR_BLUE, sd.COLOR_CYAN]
colors_names = ['Зелёный', 'Жёлтый', 'Оранжевый', 'Красный', 'Чёрный', 'Синий', 'Голубой']

for i in range(len(colors_names)):
    print(i, colors_names[i])
color = int(input("Выберите цвет: "))

polygon(300, 300, 3, 45, 100, 3, colors[color])


sd.pause()
