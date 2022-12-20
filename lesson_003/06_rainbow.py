# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
sd.caption = "Радуга"

step = 0
for color_rainbow in rainbow_colors:
    pt_start = sd.get_point(50, 50 + step)
    pt_end = sd.get_point(350, 450 + step)
    sd.line(pt_start, pt_end, color=color_rainbow, width=4)
    step += 5
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (см sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

step = 0
for color_rainbow in rainbow_colors:
    circle_center = sd.get_point(600 - step, 0 + step)
    sd.circle(circle_center, 600, color=color_rainbow,width=8)
    step += 5

sd.pause()
