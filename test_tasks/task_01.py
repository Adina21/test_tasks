# -*- coding: utf-8 -*- /python3
# Дан массив целых чисел array и целое число k. Нужно вывести все уникальные пары чисел
# из массива, сумма которых равна k.
#
# Примечание: под уникальностью понимается следующее: если ответу удовлетворяет несколько пар вида
# (a, b) и (b, a), то достаточно вывести только одну пару (a, b)

array = [1, 2, 6, 5, 3, 4, 7, 8, 3, 2]


def search_pairs(array, k):
    array_dict = {}
    for num in array:
        if num in array_dict:
            array_dict[num] += 1
        else:
            array_dict[num] = 1

    for elem in array_dict:
        addition = k - elem
        if (addition in array_dict) and (elem < addition):
            print((elem, addition))


print(search_pairs(array, 5))
