"""
В решении первой индивидуальной задачи использовать вместо input чтение с файла.

Пример:
Входные данные: 5 5 2 7 4
Выходные данные: 57.000
"""

with open("task_1_file.txt", mode="r", encoding="utf-8") as file:
    g1, g2, x, z, y = [float(i.strip()) for i in file.readlines()]

area_first_rect = g1*g2
area_third_rect = z*y
area_second_rect = x * (y-x)
sum_area = area_first_rect + area_second_rect + area_third_rect

with open("task_1_file_output.txt", mode="w", encoding="utf-8") as file:
    file.write("{:.3f}".format(sum_area))

print("Выполнил Струков Артемий Викторович 2023-ФГиИБ-ПИ-1б")
