"""
ВАРИАНТЫ ИНДИВИДУАЛЬНЫХ ЗАДАНИЙ № 4a
Постановка задачи: Дан двумерный массив A размером n*m элементов, заполненный целыми случайными целыми числами из
диапазона (r1, r2). Вывести на экран исходный массив и результаты вычислений/преобразований с точностью до 3-го знака.

Указания:
1. Двумерный массив описать с использованием списочного типа данных
2. Не использовать стандартные функции min, max, sum и т.п.
(написать свои функции).
3. Результат представить в виде пользовательской функции.


Дан двумерный массив A размером 8*5 элементов, заполненный случайными целыми числами из диапазона (-100,100).
Определить, есть ли в данном массиве столбец, в котором равное количество положительных и отрицательных элементов.
"""
from random import randint


def generate_matrix(n: int, m: int) -> list[list[int]]:
    return [[randint(-100, 100) for _ in range(m)] for _ in range(n)]


def pprint(matrix: list[list[int]]):
    print("[" + "\n".join([", ".join([str(elem) for elem in line]) for line in matrix]) + "]")


def check_column(column: list[int]) -> bool:
    count_positive, count_negative = 0, 0
    for elem in column:
        if elem < 0:
            count_negative += 1
        else:
            count_positive += 1
    return count_positive == count_negative


def get_column(matrix: list[list[int]], index_column: int) -> list[int]:
    return [line[index_column] for line in matrix]


def main():
    data = generate_matrix(8, 5)

    pprint(data)
    for i in range(5):
        column = get_column(data, i)
        if check_column(column):
            print(True)
            return
    print(False)


main()

print("Выполнил Струков Артемий Викторович 2023-ФГиИБ-ПИ-1б")
