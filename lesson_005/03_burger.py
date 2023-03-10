# -*- coding: utf-8 -*-
import my_burger
# Создать модуль my_burger. В нем определить функции добавления ингредиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью функций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает ингредиентов - создать соответствующие функции в модуле my_burger
burger = my_burger.cheeseburger()
my_burger.print_burger()

fav_burger = my_burger.new_burger()
my_burger.add_ingredient(my_burger.mayonnaise)
my_burger.add_ingredient(my_burger.cutlet)
my_burger.add_ingredient(my_burger.bun)

my_burger.print_burger()
