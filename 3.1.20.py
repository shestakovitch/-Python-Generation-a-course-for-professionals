"""Функция get_min_max()
Реализуйте функцию get_min_max(), которая принимает один аргумент:

dates — список дат (тип date)

Функция должна возвращать кортеж, первым элементом которого является минимальная дата из списка dates, вторым —
максимальная дата из списка dates. Если список dates пуст, функция должна вернуть пустой кортеж.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_min_max(), но не код,
вызывающий ее."""

from datetime import date


def get_min_max(dates=list):
    return (min(dates), max(dates)) if dates else ()