# from random import randint, random, choice
choice(list)  # выбор одного значения из списка
randint(a,b)  # произвольное целое число от a до b-1
random()  # произвольное число от 0 до 1

# Интересные функции python:
x = 10
isinstance(x, int)  # проверяет является ли x переменной типа int. True/False
type(x)  # выводит тип переменной
id(x)  # получение ID элемента

x, y = map(int, input().split())  # для ввода нескольких переменных сразу

# STRING. Методы для работы со строками. Строки являются упорядоченными неизменяемыми объектами
my_string = 'Строка'
len(my_string)  # Длина строки
my_string.find('a'), my_string.rfind('a')  # Поиск в строке подстроки 'а' слева или справа
my_string.replace('a', 'b')  # заменяет в строке 'a' на 'b'
my_string.lower(), my_string.upper()  # приводит строку к нижнему или верхнему регистру
my_string.isalpha()  # Строка содержит только буквы
my_string.isdigit()  # Строка содержит только цифры
my_string.isnumeric()  # Строка числовая?

# LIST. Методы для работы со списками. Списки являются упорядоченными изменяемыми объектами
my_list = [1, 2, 3, 'Текст', 5]
my_list.extend([7, 8, 9])  # расширить список, добавив в конец списка другой список
my_list.append(6)  # Добавление элемента в конец списка
my_list += [1, 2, 3]  # а можно просто прибавить
my_list.insert(3, 'eee')  # вставить элемент на 3-й индекс, остальные сдвинутся вправо
del my_list[6]  # удалить 6-й элемент (оператором языка)
my_list.remove('Текст')  # удалить элемент со значением 'Текст'
prov_in = 5 in my_list  # проверка входит ли элемент в список
my_list = [1, 2, 3, 12, 5]
max(my_list)  # максимальный элемент
min(my_list)  # минимальный элемент
my_list.sort()  # сортирует список
# Там много всяких методов)))

# TUPLE. Методы для работы с кортежами. Кортежи являются упорядоченными неизменяемыми объектами
my_tuple = (1, 2, 3)
my_tuple += (5, 6)  # Добавить элементы в кортеж. Создаётся новый объект

# DICT. Методы для работы со словарями. Словари являются неупорядоченными изменяемыми объектами
my_dict = {}  # Пустой словарь
my_dict['слон'] = 'Elephant'
my_dict.get('слон')  # Получить значение по ключу
my_dict.setdefault('кот', 'Cat')  # Получает значение, если оно есть. Добавляет, если его нет

# SET. Методы для работы с множествами. Множества являются неупорядоченными изменяемыми объектами
my_set = set()  # Создание множества
my_other_set = set([1, 2, 3, 4, 5, 5, 5, 5, 5, 6, 6, 7, 8, 9, 0])
# ИЛИ
my_another_set = {1, 2, 3, 4, 5, 5, 5, 5, 5, 6, 6, 7, 8, 9, 0}
# Основные операции
union = my_set | my_other_set  # Объединение
intersection = my_set & my_other_set  # Пересечение
difference = my_set - my_other_set  # Вычитание

prov = 5 in my_set  # проверка входит ли элемент в множество

# Основные методы
my_set.add(1)  # Добавление элемента
my_set.pop()  # Удаление элемента, возвращает полученное множество
my_set.discard(2)  # Удаление элемента если он во множестве. Если нет, то ничего не делает
my_set.update()  # Обновляет множество объединением с другим

# Полезные функции для работы с атрибутами класса
hasattr(object, name)  # проверка существования
setattr(object, name, value)  # установка
delattr(object, name)  # удаление
# name это строка!

# Специальные методы для класса
# Такие методы выглядят как __имя__()
object.__init__()  # - конструктор , который автоматически вызывается при создании объекта-экземпляра
object.__del__(self)  # - вызывается перед уничтожением объекта
object.__str__   # - вызывается при преобразовании объекта к строке str(obj), например, print(my_backpack)
object.__len__   # - вызывается для получения "размера" объекта с помощью функции len()
object.__hash__  # - вызывается для получения уникального хэша объекта с помощью функции hash()
                 #   или для операций с хэширующими коллекциями - множества и словари
object.__bool__  # - вызывается для получения "истинности" объекта с помощью функции bool()

# Эмуляция операций и операторов python с помощью специальных методов
# Эмуляция операторов сравнения
object.__eq__(self, other)  # - равенство двух объектов ==
object.__ne__(self, other)  # - не равно !=
object.__lt__(self, other)  # - строго меньше <
object.__le__(self, other)  # - меньше или равно <=
object.__gt__(self, other)  # - строго больше >
object.__ge__(self, other)  # - больше или равно >=
# должны возвращать boolean - True/False

# Эмуляция математических операций
object.__add__(self, other)  # - сложение +
object.__sub__(self, other)  # - вычитание -
object.__mul__(self, other)  # - умножение *
object.__truediv__(self, other)  # - деление /
object.__floordiv__(self, other)  # - целочисленное деление //
object.__mod__(self, other)  # - остаток от деления %
object.__pow__(self, other)  # - возведение в степень **
object.__lshift__(self, other)  # - побитовый сдвиг влево <<
object.__rshift__(self, other)  # - побитовый сдвиг вправо >>
object.__and__(self, other)  # - побитовое И &
object.__xor__(self, other)  # - побитовое исключающее ИЛИ ^
object.__or__(self, other)  # - побитовое ИЛИ |
# должны возвращать объект

# для операций расширенного присвоения служат методы
object.__iadd__(self, other)  # +=
object.__isub__(self, other)  # -=
object.__imul__(self, other)  # *=
object.__itruediv__(self, other)  # /+
object.__ifloordiv__(self, other)  # //=
object.__imod__(self, other)  # %=
object.__ipow__(self, other)  # **=
object.__ilshift__(self, other)  # <<=
object.__irshift__(self, other)  # >>=
object.__iand__(self, other)  # &=
object.__ixor__(self, other)  # ^=
object.__ior__(self, other)  # |=
# они изменяют сам объект (по месту, inplace)
