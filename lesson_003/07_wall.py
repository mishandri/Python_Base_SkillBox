# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

for i in range(7):
    for j in range(15):
        ld_point = sd.get_point(0+i*100-j%2*50, 0+j*50)
        rd_point = sd.get_point(100+i*100-j%2*50, 50+j*50)
        sd.rectangle(ld_point, rd_point, width=2, color=sd.COLOR_ORANGE)
sd.pause()
