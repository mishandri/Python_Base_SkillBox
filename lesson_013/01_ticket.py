# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor

# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru


def make_ticket(fio, from_, to, date):
    path = f'lesson_013/'
    images = f'images/'
    fonts = f'fonts/'
    im = Image.open(f"{path}{images}ticket_template.png")
    
    font_path = f"{path}{fonts}/Montserrat Alternates.ttf"
    font = ImageFont.FreeTypeFont(font_path, size=20)
    font_small = ImageFont.FreeTypeFont(font_path, size=15)
    draw = ImageDraw.Draw(im)
    draw.text((50, 120), f'{fio}', font=font, fill='#000000')
    draw.text((50, 185), f'{from_}', font=font, fill='#000000')
    draw.text((50, 250), f'{to}', font=font, fill='#000000')
    draw.text((260, 255), f'{date}', font=font_small, fill='#000000')


    # im.show()
    im.save(f"{path}{images}ticket_{fio}.png")

    # print(im.format, im.size, im.mode)


# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.

make_ticket('Иванов Иван Иванович', 'г. Архангельск', 'г.Самара', '19.02.2023')