# -*- coding: utf-8 -*- /python3
# Есть файл с именами (https://yadi.sk/i/97rbNP2ucGoAKw).
# Нужно выполнить следующие действия и посчитать результат:
# 1) Отсортировать все имена в лексикографическом порядке
# 2) Посчитать для каждого имени алфавитную сумму –
# сумму порядковых номеров букв (MAY: 13 + 1 + 25 = 39)
# 3) Умножить алфавитную сумму каждого имени на порядковый номер имени в отсортированном
# списке (индексация начинается с 1). Например, если MAY находится на 63 месте в списке,
# то результат для него будет 63 * 39 = 2457.
# 4) Просуммировать произведения из третьего пункта по всем именам из файла.
#
# В качестве ответа надо прислать код и число из пункта 4
from pprint import pprint


class Result:
    def __init__(self, file_name):
        self.file_name = file_name
        self.names = []

    def run(self):
        self.sort_name()
        return self.sum_multiplication()

    def sort_name(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            for line in file:
                self.names = line.split(',')
                self.names.sort()
            return self.names

    def alphabetical_sum(self):
        alphabetical_sum = {}
        sum = 0
        for name in self.names:
            for char in name:
                if char.isalpha():
                    sum += ord(char) - ord('A') + 1
            if name not in alphabetical_sum:
                alphabetical_sum[name] = sum
            sum = 0
        return alphabetical_sum

    def serial_number_multiplication(self):
        mult_list = []
        names_dict = self.alphabetical_sum()
        for index, name in enumerate(self.names):
            mult = names_dict[name] * (index + 1)
            mult_list.append(mult)
        return mult_list

    def sum_multiplication(self):
        sum = 0
        mult_list = self.serial_number_multiplication()
        for elem in mult_list:
            sum += elem
        return (sum)


res = Result('names.txt')
print(res.run())
res.sort_name()
# Ответ: число из пункта 4 = 871853874
