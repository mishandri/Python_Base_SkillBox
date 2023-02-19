import os
from PIL import Image, ImageDraw, ImageFont

im = Image.open(f"lesson_013/python_snippets/post_card.jpg")
print(im.format, im.size, im.mode)

w, h = im.size
resized_im = im.resize((w//2, h//2))

print(resized_im.format, resized_im.size, resized_im.mode)

draw = ImageDraw.Draw(resized_im)
path = os.path.join('lesson_013','python_snippets')
font_path = os.path.join(path ,'fonts','ofont_ru_DS Eraser2.ttf')
font = ImageFont.FreeTypeFont(font_path, size=30)

x = resized_im.size[0]//2 - font.size
y = resized_im.size[1]//2 + 50

draw.text((x, y), 'Привет!', font=font, fill="#ff0000")

resized_im.show()
# resized_im.save(os.path.join(path,'probe.jpg'))