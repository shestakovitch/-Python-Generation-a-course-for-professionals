"""Функция remove_marks()
Реализуйте функцию remove_marks(), которая принимает два аргумента в следующем порядке:

text — произвольная строка
marks — набор символов
Функция должна возвращать строку text, предварительно удалив из нее все символы, перечисленные в строке marks.

Также функция remove_marks() должна иметь атрибут count, представляющий собой количество вызовов данной функции.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию remove_marks(), но не код,
вызывающий ее."""


def remove_marks(text: str, marks: str):
    remove_marks.__dict__.setdefault('count', 0)
    for mark in marks:
        text = text.replace(mark, '')
    remove_marks.count += 1
    return text