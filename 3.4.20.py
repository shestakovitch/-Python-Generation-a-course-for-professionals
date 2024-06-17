"""Соседние даты
Дана последовательность дат. Напишите программу, которая создает и выводит список, элементами которого являются неотрицательные целые числа — количество дней между двумя соседними датами последовательности.

Формат входных данных
На вход программе подается последовательность дат, разделенных пробелом, в формате DD.MM.YYYY.

Формат выходных данных
Программа должна вывести список, содержащий неотрицательные целые числа, каждое из которых — количество дней между двумя
 соседними датами последовательности.

Примечание 1. Даты в последовательности могут располагаться в произвольном порядке, то есть не гарантируется, что
следующая дата больше предыдущей.

Примечание 2. Если последовательность состоит из одной даты, то программа должна вывести пустой список.

Примечание 3. Рассмотрим второй тест, в котором подается последовательность из пяти дат. Определим элементы
результирующего списка:

первый элемент — 1, количество дней между датами 06.10.2021 и 05.10.2021
второй элемент — 3, количество дней между датами 05.10.2021 и 08.10.2021
третий элемент — 1, количество дней между датами 08.10.2021 и 09.10.2021
четвертый элемент — 2, количество дней между датами 09.10.2021 и 07.10.2021"""

from datetime import datetime, timedelta


dates = [datetime.strptime(dt, '%d.%m.%Y') for dt in input().split()]
diffs = [abs(dates[i + 1] - dates[i]).days for i in range(len(dates) - 1)]
print(diffs)