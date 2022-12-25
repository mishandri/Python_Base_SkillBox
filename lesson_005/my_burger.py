# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления ингредиентов:
bun = 'Булочка'
cutlet = 'Котлетка'
cucumber = 'Огурчик'
tomato = 'Помидорчик'
mayonnaise = 'Майонез'
cheese = 'Сыр'
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."
burger = []

def new_burger():
    burger.clear()


def add_ingredient(ingredient):
    burger.append(ingredient)


def print_burger():
    print("Бургер: ", burger)

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью функций из my_burger и вывести на консоль.
def cheeseburger():
    new_burger()
    add_ingredient(bun)
    add_ingredient(cheese)
    add_ingredient(cutlet)
    add_ingredient(mayonnaise)
    add_ingredient(cucumber)
    add_ingredient(cheese)
    add_ingredient(cutlet)
    add_ingredient(bun)

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает ингредиентов - создать соответствующие функции в модуле my_burger
