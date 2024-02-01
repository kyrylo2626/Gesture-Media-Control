import sys
from PyQt5 import QtWidgets


app = QtWidgets.QApplication(sys.argv)

from Client.Controller.AppUIController import AppUIController

start_window = AppUIController()
sys.exit(app.exec_())