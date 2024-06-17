"""Комментатор
Дан блок кода на языке Python. Напишите программу, которая определяет количество строк в данном коде, которые содержат в
 себе только комментарии. Если в строке помимо комментария имеется что-то еще, то такую строку учитывать не нужно.

Формат входных данных
На вход программе подается произвольное количество строк, в совокупности представляющих блок кода на языке Python.

Формат выходных данных
Программа должна вывести единственное число — количество строк в введенном коде, которые содержат в себе только
комментарии."""

import sys

print(sum(line.strip().startswith('#') for line in sys.stdin))