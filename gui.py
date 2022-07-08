#!/usr/bin/python3
import sys

from PySide2 import QtWidgets
from calculator import Calculator
from viewer import Viewer


class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(GUI, self).__init__()
        self.setWindowTitle('Code Test')

        w = QtWidgets.QWidget()
        page1 = Calculator()
        page2 = Viewer()

        tab = QtWidgets.QTabWidget()
        tab.addTab(page1, 'Calculator')
        tab.addTab(page2, 'Viewer')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(tab, 1)
        w.setLayout(layout)

        self.setCentralWidget(w)


if '__main__' == __name__:
    app = QtWidgets.QApplication(sys.argv)
    main = GUI()
    main.show()

    ret = app.exec_()
    sys.exit(ret)
