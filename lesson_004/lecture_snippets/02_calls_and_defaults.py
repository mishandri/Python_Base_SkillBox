# -*- coding: utf-8 -*-


# Способы вызова функций
def vector_module(x, y, z):
    return (x ** 2 + y ** 2 + z ** 2) ** .5


# позиционные параметры
res = vector_module(2, 3, 4)
print(res)

# именованные параметры
res = vector_module(x=2, y=3, z=4)
print(res)

# если параметры именованные, то порядок неважен
res = vector_module(z=4, x=2, y=3)
print(res)

# можно совмещать
res = vector_module(2, 3, z=4)
print(res)


# можно потребовать, что бы при вызове некоторые параметры указывались явно
# это будут все параметры, которые идут после *
def vector_module(x, y, *, z):
    return (x ** 2 + y ** 2 + z ** 2) ** .5


# не пройдёт
res = vector_module(2, 3, 4)
# все нормально
res = vector_module(2, 3, z=4)
res = vector_module(z=4, x=2, y=3)


# можно потребовать указание всех параметров явно
def vector_module(*, x, y, z):
    return (x ** 2 + y ** 2 + z ** 2) ** .5


# не пройдёт
res = vector_module(2, 3, 4)
res = vector_module(2, 3, z=4)
# все нормально
res = vector_module(z=4, x=2, y=3)


# неправильные вызовы функций
# res = vector_module()  # не передали ни одного параметра
# res = vector_module(2, 3)  # передали мало параметров
# res = vector_module(2, 3, 3, 4)  # передали много параметров
# res = vector_module(x=2, y=3, x=4)  # повтор параметра
# res = vector_module(2, 3, x=4)  # повтор параметра
# res = vector_module(2, y=3, 4)  # позиционный параметр идет после именованного
# res = vector_module(x=2, y=3, z=5, dist=4)  # неизвестное имя параметра