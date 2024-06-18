"""Функция custom_sort() 🌶️
Реализуйте функцию custom_sort(), которая принимает два аргумента в следующем порядке:

ordered_dict — словарь OrderedDict
by_values — булево значение, по умолчанию имеет значение False
Функция должна сортировать словарь ordered_dict:

по ключам, если by_values имеет значение False
по значениям, если by_values имеет значение True
Примечание 1. Функция должна изменять переданный словарь, а не возвращать новый. Возвращаемым значением функции должно
быть None.

Примечание 2. Гарантируется, что переданный в функцию словарь можно отсортировать, то есть он не содержит ключи, имеющие
разные типы, а также значения, имеющие разные типы.

Примечание 3. Если два элемента имеют равные значения, то следует сохранить их исходный порядок следования.

Примечание 4. В тестирующую систему сдайте программу, содержащую только необходимую функцию custom_sort(), но не код,
вызывающий ее."""

from collections import OrderedDict


def custom_sort(ordered_dict=OrderedDict, by_values=False):
    if by_values:
        for value in sorted(ordered_dict, key=lambda x: ordered_dict[x]):
            ordered_dict.move_to_end(value)
    else:
        for key in sorted(ordered_dict):
            ordered_dict.move_to_end(key)
    return ordered_dict