# -*- coding: utf-8 -*-            
# @Time : 2023/8/28 15:37
# @Author : IoT_H2
# @FileName: main.py.py
# @Software: PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread,pyqtSignal

from UI import start
from UI import KeyLayout

class START(QMainWindow,start.Ui_MainWindow):
    def __init__(self):
        self.matrix = {
            "up": "[[7,8,9],[4,5,6],[1,2,3]]",
            "left": "[[9,6,3],[2,5,8],[7,4,1]",
            "right": "[[1,4,7],[2,5,8],[3,6,9]]",
            "down": "[[3,2,1],[4,5,6],[9,8,7]]"
            }

        super(START, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: {self.hide(), })
        self.pushButton_2.clicked.connect(lambda: {self.hide(), })
        self.pushButton_3.clicked.connect(lambda: {self.hide(), })
        self.pushButton_4.clicked.connect(lambda: {self.hide(), })




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = START()
    main.show()
    sys.exit(app.exec_())


