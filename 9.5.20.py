"""Функция sort_priority() 🌶️
Реализуйте функцию sort_priority(), которая принимает два аргумента в следующем порядке:

values — список чисел
group — список, кортеж или множество чисел
Функция должна сортировать по неубыванию список чисел values, делая при этом приоритетной группу чисел из group, которая
должна следовать первой.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию sort_priority(), но не код,
вызывающий ее."""


def sort_priority(values: list, group):
    values_max, group_max = max(values), max(group)
    values.sort(key=lambda x: x if x in group else x + group_max + values_max)