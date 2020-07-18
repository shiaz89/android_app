import pyowm
import sys

from PySide2 import QtWidgets, QtCore, QtGui

from test import Ui_Dialog

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    def get_weather_city():
        owm = pyowm.OWM('240b25078b2feec50d1e6a658e9a010b')
        mgr = owm.weather_manager()
        city = ui.lineEdit.text() if ui.lineEdit.text() else 'Санкт-Петербург'
        observation = mgr.weather_at_place(city)
        w = observation.weather
        temperature = w.temperature('celsius')['temp']

        ui.label.setText(f'Температура в городе {city}: {temperature}')

    ui.pushButton.clicked.connect(get_weather_city)
    sys.exit(app.exec_())
