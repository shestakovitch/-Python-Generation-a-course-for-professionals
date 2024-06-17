"""Лемма о трёх носках
Анри и Дима, имея на руках ящик с бесконечным количеством носков, решили сыграть в игру. Ребята по очереди достают из
ящика произвольное количество носков, и после неопределенного числа ходов игра заканчивается. Если тот, кто сделал
последний ход, вытащил четное количество носков — он побеждает, в противном случае проигрывает.

Напишите программу, которая определяет победителя в данной игре, если первый ход делает Анри.

Формат входных данных
На вход программе подается произвольное количество строк, в каждой строке записано натуральное число — количество
носков, которые вытащил один из игроков.

Формат выходных данных
Программа должна определить победителя в игре, правила которой представлены в условии задачи, и вывести его имя.

Примечание 1. Рассмотрим первый тест. Распишем ходы игроков:

Анри — 1
Дима — 3
Анри — 5
Дима — 10
Анри — 3
Дима — 2
Анри — 12
Побеждает Анри, так как он делает последний ход и при этом достает четное количество носков. Причем общее количество не
важно, важно лишь количество в последнем ходе."""

import sys

print('Дима' if (len(socks_box := [line.strip() for line in sys.stdin]) + int(socks_box[-1])) % 2 == 0 else 'Анри')