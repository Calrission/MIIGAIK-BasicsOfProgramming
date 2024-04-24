"""
ВАРИАНТ ИНДИВИДУАЛЬНОГО ЗАДАНИЯ № 1 (PYTHON)
Тема 1: Линейная структура алгоритма программы

Задание: написать программу вычисления объема и площади геометрической фигуры, исходя из заданных параметров.
Результат выводить с точностью 3 знака после запятой.
https://i.imgur.com/fbDT5kt.png
https://imgur.com/gndpcQb

Указание: Не использовать функцию def

Пример:
Входные данные: 5 5 2 7 4
Выходные данные: 57.000
"""

g1, g2, x, z, y = [float(i) for i in input('Введите заданные стороны: ').split(" ")]
area_first_rect = g1*g2
area_third_rect = z*y
area_second_rect = x * (y-x)
sum_area = area_first_rect + area_second_rect + area_third_rect
print("{:.3f}".format(sum_area))

print("Выполнил Струков Артемий Викторович 2023-ФГиИБ-ПИ-1б")
