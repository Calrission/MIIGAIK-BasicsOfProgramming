"""
ВАРИАНТЫ ИНДИВИДУАЛЬНЫХ ЗАДАНИЙ № 5c
Программа с использованием ООП:
тема: Алгоритм программы с ветвлениями и двумерным циклом.
тема: Списочный тип данных.
тема: Пользовательские функции.
тема: Классы, объекты, методы и атрибуты.

Задание: разработать аналогичную программу №5c табулирования,
но с использованием объектно-ориентированного подхода (и точно также с учетом области ее
определения при изменении аргумента значения х от начального x_0 до конечного значения
x_n постоянным шагом h_x, где значения функции выводить с точностью 3 знака после запятой);

x от [-20;40] шаг 0.2
"""

from numpy import arange
from math import sqrt


class Calculator:
    def __init__(self, x: float):
        self.x = x

    def calc_first_circle(self) -> float:
        # x^2+(y-1)^2=9
        # y = sqrt(9 - x^2) + 1
        return sqrt(9 - self.x ** 2) + 1

    def calc_second_circle(self) -> float:
        # (x-5)^2+(y-1)^2=4
        # y = sqrt(-21 - x**2 + 10*x) + 1
        return sqrt(-21 - self.x ** 2 + 10 * self.x) + 1

    def calc_third_circle(self) -> float:
        # (x-8)^2+(y-1)^2=1
        # y = sqrt(-63 - x**2 + 16*x) + 1
        return sqrt(-63 - self.x ** 2 + 16 * self.x) + 1

    def calc(self) -> float:
        if -3 <= self.x <= 3:
            return self.calc_third_circle()
        if 3 < self.x <= 7:
            return self.calc_second_circle()
        if 7 < self.x <= 9:
            return self.calc_third_circle()
        return 1.0


class Main:
    def __init__(self):
        self.x = None
        self.y = None

    def pprint(self):
        y = "{0:.3f}".format(self.y)
        print(f"f({self.x}) = {y}")

    def main(self):
        for x in arange(-20, 40.1, 0.2):
            self.x = float("{:.3f}".format(x))
            self.y = float("{:.3f}".format(Calculator(self.x).calc()))
            self.pprint()

    @staticmethod
    def run():
        Main().main()


if __name__ == "__main__":
    Main.run()

print("Выполнил Струков Артемий Викторович 2023-ФГиИБ-ПИ-1б")
