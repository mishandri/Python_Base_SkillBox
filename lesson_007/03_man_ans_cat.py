# -*- coding: utf-8 -*-

from random import randint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py
# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 10
        self.house = None

    def __str__(self):
        if self.is_alive:
            status = f'сытость {self.fullness}'
        else:
            status = 'мёртв'

        return f'{self.name}: {status}'

    def eat(self):
        if self.house.food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 20
            self.house.food -= 10
        else:
            print('{} нет еды'.format(self.name))
            self.shopping()

    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.house.money += 50

    def watch_tv(self):
        print('{} смотрел TV'.format(self.name))

    def go_to_the_house(self, house):
        self.house = house

        print('{} въехал в дом'.format(self.name))

    @property
    def is_alive(self) -> bool:
        return self.fullness >= 0

    def act(self):
        if not self.is_alive:
            print('{} умер...'.format(self.name))
            return

        dice = randint(1, 6)

        if self.fullness <= 20:
            self.eat()
        elif self.house.food <= 30:
            self.shopping()
        elif self.house.money <= 50:
            self.work()
        elif self.house.catfood <= 30:
            self.shopping_catfood()
        elif self.house.dirt >= 30:
            self.cleaning()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.cleaning()
        else:
            self.watch_tv()

        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            print('{} сходил в магазин'.format(self.name))
            self.house.money -= 50
            self.house.food += 50
        else:
            print('{} деньги кончились!'.format(self.name))
            self.work()

    def have_a_cat(self, cat: 'Cat'):
        if self.house is None:
            print('У меня нет дома')
        elif self.house.cat is not None:
            print('У дома есть кот')
        else:
            self.house.cat = cat
            self.house.catfood = 100
            self.house.dirt = 10
            print('{} привел в дом кота {}'.format(self.name, cat.name))

    def shopping_catfood(self):
        self.house.catfood += 50
        self.house.money -= 50
        print('{} купил еды для кота'.format(self.name))

    def cleaning(self):
        if self.house.dirt >= 100:
            self.house.dirt -= 100
        else:
            self.house.dirt = 0
        self.fullness -= 10  # потому что каждый ход -10 да ещё -10 = -20

        print('{} убрался в доме'.format(self.name))


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return '{}: сытость {}'.format(self.name, self.fullness)

    @property
    def is_alive(self) -> bool:
        return self.fullness >= 0

    def eat(self):
        self.fullness += 20
        my_sweet_home.catfood -= 10  # Это неправильно
        print('{} поел'.format(self.name))

    def dirt_house(self):
        self.fullness -= 10
        my_sweet_home.dirt += 5  # Это неправильно
        print('{} порвал обои'.format(self.name))

    def sleep(self):
        self.fullness -= 10

    def act(self):
        if self.fullness < 0:
            print('{} умер...'.format(self.name))
            return

        dice = randint(1, 6)

        if self.fullness <= 20:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.dirt_house()
        else:
            self.sleep()

        self.fullness -= 10


class House:
    def __init__(self):
        self.food = 50
        self.money = 50
        self.catfood = None
        self.dirt = None
        self.cat = None

    def __str__(self):
        return 'В доме осталось еды {}, денег {}. Еды для кота {}. Грязь {}'.format(
            self.food, self.money, self.catfood, self.dirt)


# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризуется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни')
]

my_sweet_home = House()
my_cat = Cat(name='Барсик')

for citizen in citizens:
    citizen.go_to_the_house(my_sweet_home)

citizens[0].have_a_cat(my_cat)

for day in range(1, 366):
    print('\n===================== ДЕНЬ {} ====================='.format(day))
    for citizen in citizens:
        if citizen.is_alive:
            citizen.act()
        else:
            pass
    my_cat.act()

    print(my_sweet_home)
    print('---------------------- ЖИТЕЛИ ----------------------')
    for citizen in citizens:
        print(citizen)
    print(my_cat)
