"""
ВАРИАНТ ИНДИВИДУАЛЬНОГО ЗАДАНИЯ № 2 (PYTHON)
Тема 2: Ветвления в алгоритмах программы

Задание: написать программу для расчета по двум формулам.
Результаты вычисления по обеим тригонометрическим выражениям должны совпадать.
Подготовить скрины не менее трех тестовых примеров. Результат выводить с точностью 2 знака после запятой.
https://i.imgur.com/fbDT5kt.png

Примеры
https://imgur.com/ZhOchiK
https://imgur.com/OcYE6ws
https://imgur.com/FBH9r3P

Указание: Не использовать функцию def
"""

m = float("{:.2f}".format(float(input())))
no_value_m = float("{:.2f}".format(2 / 3))
if m > 0 and m != no_value_m:
    if 0 < m < no_value_m:
        print("В промежутке m ∈ (0, 2/3), z1 < 0, а z2 > 0, так что z1 != z2 в любом случае")
    else:
        z1 = (((3 * m + 2) ** 2 - 24 * m) ** 0.5) / (3 * (m ** 0.5) - 2 / (m ** 0.5))
        z2 = m ** 0.5
        res_z1 = "{:.2f}".format(z1)
        res_z2 = "{:.2f}".format(z2)
        print(f"z1={res_z1}\nz2={res_z2}\n{z1 == z2}")
else:
    print("Введенное значение числа m не соответствует одз D(y): m ∈ (0, 2/3) V (2/3, +∞)")

print("Выполнил Струков Артемий Викторович 2023-ФГиИБ-ПИ-1б")