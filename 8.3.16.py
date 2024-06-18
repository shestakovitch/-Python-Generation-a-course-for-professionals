"""Функция to_binary()
Реализуйте функцию to_binary() с использованием рекурсии, которая принимает один аргумент:

number — неотрицательное целое число
Функция должна возвращать строковое представление числа number в двоичной системе счисления.

Примечание 1. Вспомнить алгоритм перевода числа из десятичной системы счисления в двоичную можно по ссылке."""


def to_binary(number: int):
    if number <= 1:
        return number
    else:
        return str(to_binary(number // 2)) + str(number % 2)