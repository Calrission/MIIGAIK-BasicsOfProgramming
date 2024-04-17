"""
В решении первой индивидуальной задачи использовать обработку исключений.

Пример:
Входные данные: 5 5 2 7 4
Выходные данные: 57.000
"""


with open("task_1_exception.txt", mode="r", encoding="utf-8") as file:
    g1, g2, x, z, y = [float(i.strip()) for i in file.readlines()]

with open("task_1_exception_output", mode="w", encoding="utf-8") as file:
    try:
        area_first_rect = g1*g2
        area_third_rect = z*y
        area_second_rect = x * (y-x)
        if area_first_rect <= 0:
            raise Exception(f"Площадь первого прямоугольника {area_first_rect} <= 0; Стороны: {g1} и {g2}")
        if area_second_rect <= 0:
            raise Exception(f"Площадь второго прямоугольника {area_second_rect} <= 0; Стороны: {x} и {y-x}")
        if area_third_rect <= 0:
            raise Exception(f"Площадь третьего прямоугольника {area_third_rect} <= 0; Стороны: {x} и {y-x}")
        sum_area = area_first_rect + area_second_rect + area_third_rect
        file.write("{:.3f}".format(sum_area))
    except Exception as e:
        file.write(str(e))

print("Выполнил Струков Артемий Викторович 2023-ФГиИБ-ПИ-1б")
