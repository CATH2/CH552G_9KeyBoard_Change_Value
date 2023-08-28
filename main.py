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

from function_serial import *

class START(QMainWindow,start.Ui_MainWindow):
    def __init__(self):
        self.matrix = {
            "up": [[7,8,9],[4,5,6],[1,2,3]],

            "left": [[9,6,3],[2,5,8],[7,4,1]],

            "right": [[1,4,7],[2,5,8],[3,6,9]] ,

            "down": [[3,2,1],[4,5,6],[9,8,7]]
            }

        super(START, self).__init__()
        self.setupUi(self)

        # 方向矩阵选择
        self.pushButton.clicked.connect(lambda: {self.hide(), KeyLayout(self.matrix["up"]).show()})
        self.pushButton_2.clicked.connect(lambda: {self.hide(), KeyLayout(self.matrix["left"]).show() })
        self.pushButton_3.clicked.connect(lambda: {self.hide(), KeyLayout(self.matrix["right"]).show() })
        self.pushButton_4.clicked.connect(lambda: {self.hide(), KeyLayout(self.matrix["down"]).show()})

class KeyLayout(QMainWindow,KeyLayout.Ui_MainWindow):
    class OpenSerialThread(QThread):
        def __init__(self,COM = "COM5"):
            super().__init__()
            self.COM = COM


        # 定义一个信号，用于在工作完成后发射
        work_finished = pyqtSignal()
        def run(self):
            serial_connect(self.COM)
            print("连接成功")
            # 发射工作完成信号
            self.work_finished.emit()

    class ScanSerialThread(QThread):
        def __init__(self):
            super().__init__()
            self.devices = []

        # 定义一个信号，用于在工作完成后发射
        work_finished = pyqtSignal()
        # def __init__(self):
        #     self.serials = 0

        def run(self):
            print("开始扫描串口...")
            serials = serial_scan()
            for port in serials:
                self.devices.append(port.device)

            print(self.devices)
            # 发射工作完成信号
            self.work_finished.emit()


    def __init__(self,matrix):

        print(matrix)

        super(KeyLayout, self).__init__()
        self.setupUi(self)

        self.pushButton_close.hide() # 隐藏 关闭串口


        self.pushButton_back.clicked.connect(lambda: {self.hide(), START().show()}) # 返回方向矩阵选择

        self.pushButton_scan.clicked.connect(lambda: {self.start_scan()}) # 扫描串口
        self.pushButton_open.clicked.connect(lambda: {self.start_connect()}) #打开串口

    def start_scan(self):
        print("扫描中...")
        self.worker_thread = self.ScanSerialThread()
        self.worker_thread.start()

    def start_connect(self,COM = "COM5"):
        print("连接中...")
        self.worker_thread = self.OpenSerialThread(COM)
        self.worker_thread.start()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = START()
    main.show()
    sys.exit(app.exec_())


