# -*- coding: utf-8 -*-            
# @Time : 2023/8/29 1:39
# @Author : IoT_H2
# @FileName: THREAD.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtCore import QThread,pyqtSignal
from Function.function_serial import *

class OpenSerialThread(QThread):
    def __init__(self, COM="COM5"):
        super().__init__()
        self.COM = COM

    # 定义一个信号，用于在工作完成后发射
    work_finished = pyqtSignal()

    def run(self):
        try:
            serial_connect(self.COM)
            print("连接成功")
            self.state = 1
        except:
            self.state = 0

        # 发射工作完成信号
        self.work_finished.emit()

class ScanSerialThread(QThread):
    def __init__(self):
        super().__init__()
        self.devices = []

    # 定义一个信号，用于在工作完成后发射
    work_finished = pyqtSignal()

    def run(self):
        try:
            print("开始扫描串口...")
            serials = serial_scan()
            for port in serials:
                self.devices.append(port.device)

            print(self.devices)
            # 发射工作完成信号
            self.work_finished.emit()
            self.state = 1
        except:
            self.state = 0

class Fail_Connect(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)

        self.btn_fail = QPushButton("失败", self)
        self.btn_fail.setGeometry(80, 80, 100, 30)
        self.btn_fail.clicked.connect(self.show_fail_dialog)

    def show_fail_dialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("操作失败")
        msg.setWindowTitle("失败提示")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

