"""
ВАРИАНТЫ ИНДИВИДУАЛЬНЫХ ЗАДАНИЙ № 5b
программа с функцией
тема: Алгоритм программы с ветвлениями и двумерным циклом.
тема: Списочный тип данных.
тема: Пользовательские функции.

Задание: разработать аналогичную программу №5b табулирования,
но с использованием пользовательских функций (точно также с учетом области ее определения
при изменении аргумента значения х от начального x_0 до конечного значения x_n постоянным шагом h_x,
где значения функции выводить с точностью 3 знака после запятой);

x от [-20;40] шаг 0.2
"""

from numpy import arange
from math import sqrt


def calc_first_circle(x: float) -> float:
    # x^2+(y-1)^2=9
    # y = sqrt(9 - x^2) + 1
    try:
        return sqrt(9 - x ** 2) + 1
    except ValueError:
        return 1


def calc_second_circle(x: float) -> float:
    # (x-5)^2+(y-1)^2=4
    # y = sqrt(-21 - x**2 + 10*x) + 1
    try:
        return sqrt(-21 - x ** 2 + 10 * x) + 1
    except ValueError:
        return 1


def calc_third_circle(x: float) -> float:
    # (x-8)^2+(y-1)^2=1
    # y = sqrt(-63 - x**2 + 16*x) + 1
    try:
        return sqrt(-63 - x ** 2 + 16 * x) + 1
    except ValueError as e:
        return 1


def pprint(x: float, y: float):
    y = "{0:.3f}".format(y)
    print(f"f({x}) = {y}")


def main():
    for x in arange(-20, 40.1, 0.2):
        x = float("{0:.3f}".format(x))
        if -3 <= x <= 3:
            y = calc_third_circle(x)
        elif 3 < x <= 7:
            y = calc_second_circle(x)
        elif 7 < x <= 9:
            y = calc_first_circle(x)
        else:
            y = 1.0
        pprint(x, y)


if __name__ == "__main__":
    main()

print("Выполнил Струков Артемий Викторович 2023-ФГиИБ-ПИ-1б")