import math
import sys
from math import sqrt

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.set_events()

    def set_events(self):
        self.ui.action_2.triggered.connect(self.about_authors)
        self.ui.pushButton_2.clicked.connect(self.clear_fields)
        self.ui.pushButton.clicked.connect(lambda: self.count_integral(type=1))
        self.ui.pushButton_4.clicked.connect(lambda: self.count_integral(type=2))
        self.ui.pushButton_3.clicked.connect(lambda: self.count_integral(type=0))

    def set_img(self):
        self.ui.label_6.setPixmap(QPixmap("assets/img.png"))

    def del_img(self):
        self.ui.label_6.setPixmap(QPixmap())

    def count_integral(self, type: int):
        def x_for_left():
            return a + h * i

        def x_for_right():
            return a + h * (i + 1)

        def x_for_center():
            return a + h * (i + 0.5)

        func_x = [x_for_left, x_for_center, x_for_right][type]
        s1, s2 = 1, 0  # Инициализация переменных s1 и s2, которые будут хранить суммы для последовательных итераций
        iter = 0  # Счетчик итераций
        a, b, eps = int(self.ui.lineEdit.text()), int(self.ui.lineEdit_2.text()), float(self.ui.lineEdit_3.text().replace(',', '.'))
        n = 4  # Начальное количество разбиений интервала
        while abs(s2 - s1) >= eps:  # Пока разница между последовательными суммами не станет меньше заданной точности
            s1, s2 = s2, 0  # Обновление s1 и сброс s2 для новой итерации
            n *= 2  # Удвоение количества разбиений для увеличения точности
            h = (b - a) / n  # Вычисление ширины прямоугольника
            iter += 1  # Увеличение счетчика итераций
            i = 0  # Счетчик для цикла по разбиениям
            while i < n:  # Цикл по всем прямоугольникам
                x = func_x()  # Вычисление середины текущего прямоугольника
                # Вычисление значения функции в середине прямоугольника
                k = (0.5 + sqrt(x))/(1 + math.log(x, math.e)**2)
                s2 += k * h  # Добавление площади текущего прямоугольника к сумме
                i += 1  # Переход к следующему прямоугольнику
        ans = f'\nЗначение интеграла: {s2:.3f}\nКоличество итераций: {iter}'
        self.ui.label_5.setText(ans)
        self.set_img()


    def about_authors(self):
        QMessageBox.about(self, "Об авторах", "Программа была выполнена студентом:\n Струков Артемий 2023-ФГиИБ-ПИ-1б")

    def clear_fields(self):
        self.ui.lineEdit.setText('')
        self.ui.lineEdit_2.setText('')
        self.ui.lineEdit_3.setText('')
        self.ui.label_5.setText('')
        self.del_img()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
