#!/usr/bin/python3
import sys
import os

from PySide2 import QtWidgets


class Viewer(QtWidgets.QWidget):
    def __init__(self):
        super(Viewer, self).__init__()
        self.setWindowTitle('Viewer')

        # layouts
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        row1 = QtWidgets.QHBoxLayout()
        layout.addLayout(row1)
        row2 = QtWidgets.QHBoxLayout()
        layout.addLayout(row2)

        # row1 elements
        self.output = QtWidgets.QTextEdit()
        row1.addWidget(self.output)

        # row2 elements
        btn_load = QtWidgets.QPushButton('Load')
        btn_load.clicked.connect(self.load)
        row2.addWidget(btn_load)

    def load(self):
        homedir = os.path.expanduser("~")
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(
            parent=self,
            caption='Open file',
            dir=homedir,
            filter='Text files (*.txt *.py)'
        )
        if filename:
            fd = os.open(filename, os.O_RDONLY)

            n = 52428800  # 50mb

            # Read at most n bytes
            # from file descriptor
            read_bytes = os.read(fd, n)

            # Print file's content into the text box
            self.output.setText(read_bytes.decode())

            # Close the file descriptor
            os.close(fd)


if '__main__' == __name__:
    app = QtWidgets.QApplication(sys.argv)
    w = Viewer()
    w.show()

    ret = app.exec_()
    sys.exit(ret)
