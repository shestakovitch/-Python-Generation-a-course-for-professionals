"""Функция get_weekday()
Реализуйте функцию get_weekday(), которая принимает один аргумент:

number — целое число (от 1 до 7 включительно)
Функция должна возвращать полное название дня недели на русском, который соответствует числу number, при этом:

если number не является целым числом, функция должна возбуждать исключение:
TypeError('Аргумент не является целым числом')
если number является целым числом, но не принадлежит отрезку [1;7], функция должна возбуждать исключение:
ValueError('Аргумент не принадлежит требуемому диапазону')
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_weekday(), но не код,
вызывающий ее."""


def get_weekday(number: int):
    days = ('', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    if not isinstance(number, int):
        raise TypeError('Аргумент не является целым числом')
    if number < 1 or number > 7:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    return days[number]