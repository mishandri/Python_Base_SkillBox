# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

import district.central_street.house1.room1 as csh1r1
import district.central_street.house1.room2 as csh1r2
import district.central_street.house2.room2 as csh2r1
import district.central_street.house2.room2 as csh2r2
import district.soviet_street.house1.room1 as ssh1r1
import district.soviet_street.house1.room2 as ssh1r2
import district.soviet_street.house2.room1 as ssh2r1
import district.soviet_street.house2.room2 as ssh2r2

raion = []
raion.extend(csh1r1.folks + csh1r2.folks + csh2r1.folks + csh2r2.folks +
             ssh1r1.folks + ssh1r2.folks + ssh2r1.folks + ssh2r2.folks)

print(', '.join(raion))





