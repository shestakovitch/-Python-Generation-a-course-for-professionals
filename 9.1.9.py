"""Функция non_negative_even()
Реализуйте функцию non_negative_even(),  которая принимает один аргумент:

numbers — непустой список чисел
Функция должна возвращать True, если все числа в списке numbers являются четными и неотрицательными, или False в
противном случае.

Примечание 1. В задаче удобно воспользоваться функцией all().

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию non_negative_even(), но не
код, вызывающий ее."""


def non_negative_even(numbers: list):
    return all(number >= 0 and number % 2 == 0 for number in numbers)