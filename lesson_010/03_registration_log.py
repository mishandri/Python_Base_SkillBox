# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутствуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутствуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


with open('registrations_good.log', 'w', encoding='utf8'):
    pass

with open('registrations_bad.log', 'w', encoding='utf8'):
    pass

with open('registrations.txt', 'r', encoding='utf8') as file:
    for line in file:
        try:
            name, email, age = line.split(' ')
            if not name.isalpha():
                raise NotNameError('Поле имени содержит НЕ только буквы.')
            if '@' not in email or '.' not in email:
                raise NotEmailError('Поле емейл НЕ содержит @ и .(точку)')
            if not (10 <= int(age) <= 99):
                raise ValueError('поле возраст НЕ является числом от 10 до 99')
        except ValueError as exc:
            with open('registrations_bad.log', 'a', encoding='utf8') as file:
                file.write(f'{exc}\n')
        except NotNameError as exc:
            with open('registrations_bad.log', 'a', encoding='utf8') as file:
                file.write(f'{exc}\n')
        except NotEmailError as exc:
            with open('registrations_bad.log', 'a', encoding='utf8') as file:
                file.write(f'{exc}\n')
        else:
            with open('registrations_good.log', 'a', encoding='utf8') as file:
                file.write(f'{name} {email} {age}')