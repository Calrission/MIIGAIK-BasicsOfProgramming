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
        self.ui.pushButton.clicked.connect(self.count_integral)

    def set_img(self):
        self.ui.label_6.setPixmap(QPixmap("Graphics/img.png"))

    def del_img(self):
        self.ui.label_6.setPixmap(QPixmap())

    def count_integral(self):
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
                x = a + h * (i + 0.5)  # Вычисление середины текущего прямоугольника
                k = sqrt(math.log(1.1 + math.tan(x/2), math.e))  # Вычисление значения функции в середине прямоугольника

                s2 += k * h  # Добавление площади текущего прямоугольника к сумме

                i += 1  # Переход к следующему прямоугольнику
        ans = f'\nЗначение интеграла: {s2:.3f}\nКоличество итераций: {iter}'
        self.ui.label_5.setText(ans)

        self.set_img()

    def about_authors(self):
        QMessageBox.about(self, "Об авторах", "Программа была выполнена студентом:\n Зиновьев Данил 2023-ФГиИБ-ИСиТ-1б")

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
