"""Количество дней 😉
Напишите программу, которая определяет количество дней в заданном месяце.

Формат входных данных
На вход программе подаются год и порядковый номер месяца (начиная с 1), разделенные пробелом.

Формат выходных данных
Программа должна вывести единственное число — количество дней в введенном месяце.

Примечание 1. Январь имеет порядковый номер 1, Февраль — 2, Март — 3, и так далее."""

import calendar

print(calendar.monthrange(*map(int, input().split()))[1])