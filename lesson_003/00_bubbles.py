# -*- coding: utf-8 -*-

import simple_draw as sd

sd.caption = "Пузырьки"
sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(300, 300)
# radius = 50
# for _ in range(3):
#     radius += 5
#     sd.circle(point, radius)


# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(point, radius, width=2)


# bubble(point, 10)

# Нарисовать 10 пузырьков в ряд
# for x in range(1,11):
#     point = sd.get_point(x * 100, 100)
#     bubble(point, 5)

# Нарисовать три ряда по 10 пузырьков
# for y in range(1,4):
#     for x in range(1,11):
#         point = sd.get_point(x * 100, y * 100)
#         bubble(point, 5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    bubble(point, 5)

sd.pause()
