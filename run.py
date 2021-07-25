import os
import sys
from option_ui import Ui_Form
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication


class Main_window(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton_pn.clicked.connect(self.OpenPn)
        self.pushButton_mos.clicked.connect(self.OpenMos)
        self.pushButton_bjt.clicked.connect(self.OpenBjt)
        self.pushButton_quit.clicked.connect(QCoreApplication.instance().quit)

    def OpenPn(self):
        os.system("python ./PN_junction/PN.py")

    def OpenMos(self):
        os.system("python ./MOS/MOS.py")

    def OpenBjt(self):
        os.system("python ./BJT/BJT.py")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main_window()
    main_window.show()
    app.exec()
