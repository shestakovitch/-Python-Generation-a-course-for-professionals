"""Размах данных
Дана последовательность дат. Напишите программу, которая выводит количество дней между максимальной и минимальной датами
данной последовательности.

Формат входных данных
На вход программе подается произвольное количество строк, в каждой строке записана дата в ISO формате (YYYY-MM-DD).

Формат выходных данных
Программа должна вывести единственное число — количество дней между максимальной и минимальной датами введенной
последовательности."""

from datetime import datetime
import sys

dates = [datetime.fromisoformat(i.strip()) for i in sys.stdin.readlines()]
print((max(dates) - min(dates)).days)