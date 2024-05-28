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
import dataclasses


@dataclasses.dataclass
class Num:
    value: int | str
    base: int = 10

    def set_decimal(self):
        if self.base == 10:
            return
        self.value = int(self.value, self.base)
        self.base = 10

    def set_hex(self):
        if self.base == 16:
            return
        if self.base != 10:
            self.set_decimal()
        self.value = hex(self.value)[2:].upper()
        self.base = 16

    def set_bin(self):
        if self.base != 10:
            self.set_decimal()
        self.value = bin(self.value)[2:]
        self.base = 2

    def __eq__(self, other) -> bool:
        if isinstance(other, Num):
            return self.value == other.value and self.base == other.base
        raise Exception("Num сравнивается только с Num!")

    def __lt__(self, other):
        if isinstance(other, Num):
            if other.base != self.base:
                raise Exception("Num'ы сравниваются только когда имеют одну систему счисления")
            return self.value < other.value
        raise Exception("Num сравнивается только с Num!")

    def __le__(self, other):
        return self < other and self == other

    def __gt__(self, other):
        if isinstance(other, Num):
            if other.base != self.base:
                raise Exception("Num'ы сравниваются только когда имеют одну систему счисления")
            return self.value > other.value
        raise Exception("Num сравнивается только с Num!")

    def __ge__(self, other):
        return self > other and self == other

    def __add__(self, other):
        if isinstance(other, Num):
            if other.base != self.base:
                raise Exception(
                    "Арифметические действия с Num осуществляются только когда они имеют одну систему счисления"
                )
            return Num(self.value + other.value, self.base)
        raise Exception("Арифметические действия с Num возможно только с другим Num")

    def __neg__(self):
        return Num(self.value * (-1), self.base)

    def __sub__(self, other):
        return self + (-other)

    def __str__(self):
        return f"{self.value}_{self.base}"


def task_1():
    print("Задание 1:")
    target = Num("1111", 2)
    target_str = str(target)
    target.set_decimal()
    print(f"{target_str}\t\t=\t{target}")

    def get_check(value: Num) -> str:
        return "✅" if value == target else "❌"

    first = Num("11", 4)
    first.set_decimal()
    print(f"{get_check(first)} 11_4\t\t=\t{first}")

    second = Num("11", 10)
    second.set_decimal()
    print(f"{get_check(second)} 11_10\t=\t{second}")

    third = Num("F", 16)
    third.set_decimal()
    print(f"{get_check(third)} F_16\t\t=\t{third}")

    four = Num("17", 8)
    four.set_decimal()
    print(f"{get_check(four)} 17_8\t\t=\t{four}")

    print("-" * 8 + "Конец" + "-" * 8)


def task_2():
    print("Задание 2:")
    first = Num("1A", 16)
    first.set_decimal()
    print(f"1A_16 = {first}")
    second = Num("6", 16)
    second.set_decimal()
    print(f"6_16 = {second}")
    result = first - second
    result.set_hex()
    print(f"{first} - {second} = {result}")
    print(f"1A_16 - 6_16 = {result}")
    print("-" * 8 + "Конец" + "-" * 8)


def task_3():
    print("Задание 3:")
    first = Num("F", 16)
    first.set_decimal()
    second = Num("16", 8)
    second.set_decimal()
    if first > second:
        operation = ">"
    elif first < second:
        operation = "<"
    else:
        operation = "="
    print(f"F_16 = {first}")
    print(f"16_8 = {second}")
    print(f"F_16 {operation}")
    print("-" * 8 + "Конец" + "-" * 8)


def task_4():
    print("Задание 4:")
    first = Num("F1", 16)
    second = Num("12", 8)
    third = Num("12", 10)
    four = Num("F", 16)
    data = sorted([first, second, third, four], key=lambda num: num.value)
    print(", ".join([str(i) for i in data]))
    print(", ".join(map(str, data)))
    print("-" * 8 + "Конец" + "-" * 8)


def task_5():
    print("Задание 5:")
    value = Num("2BF8", 16)
    value.set_bin()
    print(f"2BF8_16 = {value}")
    print("-" * 8 + "Конец" + "-" * 8)


def main():
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()


if __name__ == "__main__":
    main()
