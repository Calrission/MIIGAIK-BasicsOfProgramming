"""
КР № 2
Тема: Основы объектно-ориентированного программирования (ООП)

Задание: Создайте класс ФОТОТОВАРЫ с методами, позволяющими вывести экран информацию о фототоваре, а также определить
соответствие критерию поиска. Создайте дочерние классы ФОТОАППАРАТА (производитель, модель, цена, цвет, вес),
ОБЪЕКТИВ (производитель, модель, диаметр, цена), ВИДЕОКАМЕРА (производитель, модель размер дисплея, цена, цвет)
со своими методами вывода информации на экран и определения соответствия заданной цене. Создайте список из n
фототоваров, выведите полную информацию. Организуй поиск фототовара, который может приобрести покупатељ,
имеющий заданную сумму денег.
"""


class PhotoProduct:
    def display(self):
        pass

    def equal_search(self, search_text: str) -> bool:
        pass


class PhotoCamera(PhotoProduct):
    def __init__(
            self,
            manufacture: str,
            model: str,
            price: float,
            weight: float,
            color: str
    ):
        self.manufacture = manufacture
        self.model = model
        self.price = price
        self.weight = weight
        self.color = color

    def display(self):
        print(
            f"ФОТОАППАРАТ:\n"
            f"Производитель: {self.manufacture}\n"
            f"Модель: {self.model}\n"
            f"Цвет HEX: {self.color}\n"
            f"Вес: {self.weight}г.\n"
            f"Стоимость: {self.price}₽\n"
        )

    def equal_search(self, search_text: str) -> bool:
        return str(self.price) <= search_text


class CameraLens(PhotoProduct):
    def __init__(
            self,
            manufacture: str,
            model: str,
            price: float,
            diameter: float
    ):
        self.manufacture = manufacture
        self.model = model
        self.price = price
        self.diameter = diameter

    def display(self):
        print(
            f"ОБЪЕКТИВ:\n"
            f"Производитель: {self.manufacture}\n"
            f"Модель: {self.model}\n"
            f"Диаметр: {self.diameter}мм.\n"
            f"Стоимость: {self.price}₽\n"
        )

    def equal_search(self, search_text: str) -> bool:
        return str(self.price) <= search_text


class VideoCamera(PhotoProduct):
    def __init__(
            self,
            manufacture: str,
            model: str,
            price: float,
            height_display: float,
            width_display: float,
            color: str
    ):
        self.manufacture = manufacture
        self.model = model
        self.price = price
        self.height_display = height_display
        self.width_display = width_display
        self.color = color

    def display(self):
        print(
            f"ВИДЕОКАМЕРА:\n"
            f"Производитель: {self.manufacture}\n"
            f"Модель: {self.model}\n"
            f"Цвет HEX: {self.color}\n"
            f"Размер дисплея: {self.width_display}x{self.height_display}.\n"
            f"Стоимость: {self.price}₽\n"
        )

    def equal_search(self, search_text: str) -> bool:
        return str(self.price) <= search_text


def main():
    products = [
        PhotoCamera("Sony", "X106", 2599, 100, "#ffffff"),
        PhotoCamera("Sony", "X2000", 4999, 150, "#ff1500"),
        PhotoCamera("Samsung", "GalaxyX", 5999, 500, "#000000"),
        PhotoCamera("Samsung", "GalaxyY", 10999, 200, "#000000"),
        CameraLens("Sony", "XPro", 15999, 10),
        CameraLens("Sony", "Magic10", 4999, 20),
        VideoCamera("IBM", "Blue 1011", 9999, 800, 800, "#0023ff"),
        VideoCamera("IBM", "Blue 6099", 5999, 400, 400, "#8999ff"),
    ]
    cost = input("Введите цену для поиска: ")
    for product in products:
        if product.equal_search(cost):
            product.display()


if __name__ == "__main__":
    main()
