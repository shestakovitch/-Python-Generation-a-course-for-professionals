"""Новый print
Напишите программу с использованием декоратора, которая переопределяет функцию print() так, чтобы она печатала весь
текст в верхнем регистре.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна задекорировать функцию print() так, чтобы она печатала весь текст в верхнем регистре.

Примечание 1. Значения sep и end также должны переводиться в верхний регистр.

Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а
также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов."""


def upper_print(func):
    def wrapper(*args, **kwargs):
        args_up = tuple(c.upper() if isinstance(c, str) else c for c in args)
        kwargs_up = {k: v.upper() for k, v in kwargs.items() if isinstance(v, str)}
        func(*args_up, **kwargs_up)
    return wrapper


print = upper_print(print)