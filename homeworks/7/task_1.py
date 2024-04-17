"""
Задание 1. Создать в текстовом редакторе файл, содержащий несколько строк. Определить максимальный и минимальный
размер строки в файле и вывести их в другой файл. Вывести в этот же файл все строки максимальной длины.
"""

with open("task_1_input.txt", mode="r", encoding="utf-8") as file:
    lines = [i.strip() for i in file.readlines()]

with open("task_1_output.txt", mode="w", encoding="utf-8") as file:
    line_min = min(lines, key=len)
    line_max = max(lines, key=len)
    file.write(f"Минимальная длина строки:{len(line_min)}\n{line_min}\n")
    file.write(f"Максимальная длина строки:{len(line_max)}\n{line_max}\n")