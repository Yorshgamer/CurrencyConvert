import sys
import os

from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox

class Dialogo(QDialog):
    USInUS = 1
    AusInUS = 3
    UKInUS = 1.5
    JPYInUS = 157.63500  # Nueva tasa de conversión JPY a USD
    SoInUS = 4.0  # Tasa de conversión Soles a USD
    LibInUS = 0.75  # Tasa de conversión Libras a USD
    LirInUS = 2000.0  # Tasa de conversión Liras a USD

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
        elif self.brFromPEN.isChecked():  # Nuevo: conversión desde JPY
            converted = initial / self.SoInUS
        elif self.brFromGBP.isChecked():  # Nuevo: conversión desde JPY
            converted = initial / self.LibInUS
        elif self.brFromITL.isChecked():  # Nuevo: conversión desde JPY
            converted = initial / self.LirInUS

        if self.brToUS.isChecked():
            converted = converted * self.USInUS
            self.lbCon.setText("US")
        if self.brToUK.isChecked():
            converted = converted * self.UKInUS
            self.lbCon.setText("UK")
        elif self.brToAUS.isChecked():
            converted = converted * self.AusInUS
            self.lbCon.setText("AUS")
        elif self.brToJPY.isChecked():  # Nuevo: conversión hacia JPY
            converted = converted * self.JPYInUS
            self.lbCon.setText("JPY")
        elif self.brToPEN.isChecked():  # Nueva moneda: Soles
            converted = converted * self.SoInUS
            self.lbCon.setText("PEN")
        elif self.brToGBP.isChecked():  # Nueva moneda: Libras
            converted = converted * self.LibInUS
            self.lbCon.setText("GBP")
        elif self.brToITL.isChecked():  # Nueva moneda: Liras
            converted = converted * self.LirInUS
            self.lbCon.setText("ITL")

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