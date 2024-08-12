from PyQt5.QtWidgets import QApplication
from mainframe import MainDialog
import sys


class MonitorApp(QApplication):
    def __init__(self):
        super(MonitorApp, self).__init__(sys.argv)
        self.dialog = MainDialog()
        self.dialog.show()

