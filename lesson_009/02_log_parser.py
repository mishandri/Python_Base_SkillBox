# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class log_nok:

    def __init__(self, file_log, file_res):
        self.file_log = file_log
        self.file_res = file_res
    def read_log(self):
        res = {}
        with open(self.file_log, 'r') as file:
            for line in file:
                # print(line, end='')
                if line.endswith('NOK\n'):
                    # print(line, end='')
                    if line[:17] +'] ' not in res:
                        n = 1
                    else:
                        n += 1

                    res[line[:17] + '] '] = n

            with open(self.file_res, 'w') as file_res:
                year = ''
                month = ''
                day = ''
                hour = ''
                # [2018-05-17 01:57]
                for i in res:
                    if year != i[1:5]:
                        year = i[1:5]
                        file_res.write(f'{year}\n')
                    elif month != i[6:8]:
                        month = i[6:8]
                        file_res.write(f'\t{month}\n')
                    elif day != i[9:11]:
                            day = i[9:11]
                            file_res.write(f'\t\t{day}\n')
                    elif hour != i[12:14]:
                            hour = i[12:14]
                            file_res.write(f'\t\t\t{hour}\n')
                    else:
                        file_res.write(f'\t\t\t\t{i} {res[i]}\n')

logging = log_nok('events.txt', 'res.txt')
logging.read_log()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
