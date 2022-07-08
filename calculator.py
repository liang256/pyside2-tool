#!/usr/bin/python3
import sys

from PySide2 import QtWidgets, QtGui


class Calculator(QtWidgets.QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setWindowTitle('Calculator')

        # layouts
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        row1 = QtWidgets.QHBoxLayout()
        layout.addLayout(row1)
        row2 = QtWidgets.QHBoxLayout()
        layout.addLayout(row2)

        # row1 elements
        int_validator = QtGui.QIntValidator()

        self.input_a = QtWidgets.QLineEdit('0')
        self.input_a.setValidator(int_validator)
        row1.addWidget(self.input_a)

        self.operator = QtWidgets.QComboBox()
        self.operator.addItem('+')
        self.operator.addItem('-')
        row1.addWidget(self.operator)

        self.input_b = QtWidgets.QLineEdit('0')
        self.input_b.setValidator(int_validator)
        row1.addWidget(self.input_b)

        eqaul = QtWidgets.QLabel()
        eqaul.setText('=')
        row1.addWidget(eqaul)

        self.output = QtWidgets.QLineEdit('0')
        self.output.setReadOnly(True)
        row1.addWidget(self.output)

        # row2 elements
        btn_calculate = QtWidgets.QPushButton('Calculate')
        btn_calculate.clicked.connect(self.calculate)
        row2.addWidget(btn_calculate)

    def calculate(self):
        state = '{} {} {}'.format(
            self.input_a.text(),
            self.operator.currentText(),
            self.input_b.text()
        )
        result = eval(state)

        # Update result to output widget
        self.output.setText(str(result))


if '__main__' == __name__:
    app = QtWidgets.QApplication(sys.argv)
    w = Calculator()
    w.show()

    ret = app.exec_()
    sys.exit(ret)
