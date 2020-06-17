# -*- coding: utf-8 -*- /python3
# Факториал числа n равен произведению всех чисел от 1 до n, то есть:
# n! = 1 * 2 * 3 * ... * n
# Написать функцию, которая возвращает количество идущих подряд нулей на конце n!.
# def get_zeros(n):
# ....
#
# print(get_zeros(5))
# OUT: >> 1
# print(get_zeros(12))
# OUT: >> 2


def get_zeros(n):
    count_zero = 0
    a = 5
    if n < 0:
        return False
    while n >= a:
        b = n // a
        count_zero += b
        a *= 5
    return count_zero


print(get_zeros(5))
print(get_zeros(12))