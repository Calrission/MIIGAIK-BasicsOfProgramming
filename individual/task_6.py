"""
ВАРИАНТЫ ИНДИВИДУАЛЬНЫХ ЗАДАНИЙ № 6

тема: Системы счисления на Python.

Задание: написать программу на Python с использованием пользовательских функций согласно конкретным формулировкам,
указанным перед каждым из 5 индивидуальных заданий Варианта.

Задание 1. Укажите числа, равные 1111_2 (проставьте галочки и обязательно приведите вывод):
[] 11_4 (11 в 4 системе счисления)
[] 11_10
[] F_16
[] 17_8

Задание 2. Вычислите разность (обязательно приведите вывод)
1A_16 - 6_16 = []_16

Задание 3. Восстановите пропущенный знак операции сравнения (больше, меньше, больше или равно, меньше или равно)
и обязательно приведите вывод:
F_16 [] 16_8

Задание 4. Расположите числа в порядке возрастания (обязательно приведите вывод):
F1_16; 12_8; 12_10; F_16

Задание 5. Впишите пропущенное число (обязательно приведите вывод):
2BF8_16 = []_2
"""


def to_decimal_system(value: str, base: int):
    if base == 10:
        return int(value)
    return int(value, base)


def to_hex_system(value: str | int, base: int):
    if base == 16:
        return value
    if base != 10:
        value = to_decimal_system(value, base)
    if isinstance(value, str):
        value = int(value)
    return hex(value)[2:].upper()


def decimal_to_bin(value: int) -> str:
    return bin(value)[2:]


def task_1():
    print("Задание 1:")
    target = to_decimal_system("1111", 2)
    print(f"1111_2\t\t=\t{target}_10")

    def get_check(value: int) -> str:
        return "✅" if value == target else "❌"

    first = to_decimal_system("11", 4)
    print(f"{get_check(first)} 11_4\t\t=\t{first}_10")

    second = to_decimal_system("11", 10)
    print(f"{get_check(second)} 11_10\t=\t{second}_10")

    third = to_decimal_system("F", 16)
    print(f"{get_check(third)} F_16\t\t=\t{third}_10")

    four = to_decimal_system("17", 8)
    print(f"{get_check(four)} 17_8\t\t=\t{four}_10")

    print("-" * 8 + "Конец" + "-" * 8)


def task_2():
    print("Задание 2:")
    first = to_decimal_system("1A", 16)
    print(f"1A_16 = {first}_10")
    second = to_decimal_system("6", 16)
    print(f"6_16 = {second}_10")
    result = first - second
    print(f"{first}_10 - {second}_10 = {result}_10")
    print(f"1A_16 - 6_16 = {to_hex_system(result, 10)}_16")
    print("-" * 8 + "Конец" + "-" * 8)


def task_3():
    print("Задание 3:")
    first = to_decimal_system("F", 16)
    second = to_decimal_system("16", 8)
    if first > second:
        operation = ">"
    elif first < second:
        operation = "<"
    else:
        operation = "="
    print(f"F_16 = {first}_10")
    print(f"16_8 = {second}_10")
    print(f"F_16 {operation} 16_8")
    print("-" * 8 + "Конец" + "-" * 8)


def task_4():
    print("Задание 4:")
    first = to_decimal_system("F1", 16)
    second = to_decimal_system("12", 8)
    third = to_decimal_system("12", 10)
    four = to_decimal_system("F", 16)
    to_str = {
        first: "F1_16",
        second: "F12_8",
        third: "12_10",
        four: "F_16",
    }
    data = sorted([first, second, third, four])
    print(", ".join([to_str[i] for i in data]))
    print(", ".join(map(str, data)))
    print("-" * 8 + "Конец" + "-" * 8)


def task_5():
    print("Задание 5:")
    value = to_decimal_system("2BF8", 16)
    print(f"2BF8_16 = {decimal_to_bin(value)}_2")
    print("-" * 8 + "Конец" + "-" * 8)


def main():
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()


if __name__ == "__main__":
    main()
