# -*- coding: utf-8 -*-

# параметры по умолчанию
def process(subject, action='мыла', object='раму'):
    print("Кто - ", subject)
    print("Делал(а) - ", action)
    print("Над чем - ", object)
    print("Получается :", subject, action, object)


process(subject='Мама')
process(subject='Папа', action='сломал')
process(subject='Кржижановский', action='видел', object='Ленина')  # https://goo.gl/My5Wx7


# значения по умолчанию вычисляются в точке определения функции, при компиляции
# обычная ошибка - изменяемый объект в качестве параметра по умолчанию
def add_element_to_list(element, list_to_add=[]):
    """добавляем элемент к списку"""
    list_to_add.append(element)
    return list_to_add


my_list = [3, 4, 5]
add_element_to_list(element=1, list_to_add=my_list)
print(my_list)

# new_list = add_element_to_list(element=1)
# print(new_list)
# add_element_to_list(element=7, list_to_add=new_list)
# print(new_list)

# other_new_list = add_element_to_list(element=2)
# print(other_new_list)
# print(new_list)


# решение проблемы
def add_element_to_list(element, list_to_add=None):
    """добавляем элемент к списку"""
    if list_to_add is None:
        list_to_add = []
    list_to_add.append(element)
    return list_to_add


my_list = [3, 4, 5]
add_element_to_list(element=1, list_to_add=my_list)
print(my_list)

# new_list = add_element_to_list(element=1)
# print(new_list)
# add_element_to_list(element=7, list_to_add=new_list)
# print(new_list)

# other_new_list = add_element_to_list(element=2)
# print(other_new_list)
# print(new_list)
