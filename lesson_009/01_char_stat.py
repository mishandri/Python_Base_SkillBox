# -*- coding: utf-8 -*-
import zipfile
from pprint import pprint


# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
class Stat_Txt_File:

    def __init__(self, file_name):
        self.txt_file = file_name
        self.stat = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.txt_file, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.txt_file = filename

    def collect_stat(self):
        if self.txt_file.endswith('.zip'):
            self.unzip()
        self.sequence = ''
        with open(self.txt_file, 'r', encoding='cp1251') as file:
            for line in file:
                self._collect_for_line(line=line[:-1])

    def _collect_for_line(self, line):
        for char in line:
            if char.isalpha():
                if self.sequence in self.stat:
                    if char in self.stat[self.sequence]:
                        self.stat[self.sequence][char] += 1
                    else:
                        self.stat[self.sequence][char] = 1
                else:
                    self.stat[self.sequence] = {char: 1}
                self.sequence = self.sequence[1:] + char

    def prepare(self):
        self.totals = {}
        self.stat_for_generate = {}
        for sequence, char_stat in self.stat.items():
            self.totals[sequence] = 0
            self.stat_for_generate[sequence] = []
            for char, count in char_stat.items():
                self.totals[sequence] += count
                self.stat_for_generate[sequence].append([count, char])
                self.stat_for_generate[sequence].sort(reverse=True)
        self.totals.pop('')  # Удалить пустой ключ
        # return self.totals

    def __str__(self):
        output = ''
        output += '+---------+----------+\n'
        output += '|  буква  | частота  |\n'
        output += '+---------+----------+\n'
        for key, value in self.totals.items():
            output += f'|{key:^9}|{value:^10}|\n'
        output += '+---------+----------+\n'
        return output

    #  - по частоте по возрастанию
    def sort_value(self):
        '''Sort stat by sequence'''
        self.totals = dict(sorted(self.totals.items(), key=lambda item: item[1]))

    #  - по алфавиту по возрастанию
    def sort_key_up(self):
        '''Sort stat by aplphabet'''
        self.totals = dict(sorted(self.totals.items()))

    #  - по алфавиту по убыванию
    def sort_key_down(self):
        '''Sort stat by reverse aplphabet'''
        self.totals = dict(sorted(self.totals.items(), reverse=True))


stat = Stat_Txt_File(file_name='voyna-i-mir.txt.zip')
stat.collect_stat()
stat.prepare()
# print(stat)
stat.sort_value()
print(stat)

# После выполнения первого этапа нужно сделать упорядочивание статистики
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
# Не использовал шаблонный метод
