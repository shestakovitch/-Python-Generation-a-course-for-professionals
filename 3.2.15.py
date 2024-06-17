"""Функция is_correct()
Реализуйте функцию is_correct(), которая принимает три аргумента в следующем порядке:

day — натуральное число, день
month — натуральное число, месяц
year — натуральное число, год
Функция должна возвращать True, если дата с компонентами day, month и year является корректной, или False в противном
случае.

Примечание 1. Вспомните про конструкцию try-except.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_correct(), но не код,
вызывающий ее."""


from datetime import date


def is_correct(day=int, month=int, year=int):
    try:
        date(year, month, day)
        return True
    except:
        return False