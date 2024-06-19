import sys
import os

from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox

class Dialogo(QDialog):
    AusInUS = 3
    UKInUS = 1.5
    JPYInUS = 157.63500  # Nueva tasa de conversión JPY a USD

    def __init__(self):
        super().__init__()
        ruta = os.path.dirname(os.path.abspath(__file__)) + r"\..\vista\currencyConvert.ui"
        uic.loadUi(ruta, self)

        self.pbConvert.clicked.connect(self.calculate_convert)
        self.pbExit.clicked.connect(self.exit_app)

    def calculate_convert(self):
        initial = float(self.ltAmount.text())
        converted = initial

        if self.brFromUK.isChecked():
            converted = initial / self.UKInUS
        elif self.brFromAUS.isChecked():
            converted = initial / self.AusInUS
        elif self.brFromJPY.isChecked():  # Nuevo: conversión desde JPY
            converted = initial / self.JPYInUS

        if self.brToUK.isChecked():
            converted = converted * self.UKInUS
        elif self.brToAUS.isChecked():
            converted = converted * self.AusInUS
        elif self.brToJPY.isChecked():  # Nuevo: conversión hacia JPY
            converted = converted * self.JPYInUS

        self.lbResult.setText(f"{converted:.5f}")

    def exit_app(self):
        resultado = QMessageBox.question(self, "Salir", "¿Está seguro que desea salir?", QMessageBox.StandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No))
        if resultado == QMessageBox.StandardButton.Yes:
            sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = Dialogo()
    dialogo.show()
    sys.exit(app.exec())