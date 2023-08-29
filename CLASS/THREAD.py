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
            self.ser = serial_connect(self.COM)
            print("连接成功")
            self.state = 1
        except:
            self.state = 0

        # 发射工作完成信号
        self.work_finished.emit()

class ScanSerialThread(QThread):
    def __init__(self):
        super().__init__()
        self.devices = set()

    # 定义一个信号，用于在工作完成后发射
    work_finished = pyqtSignal()

    def run(self):
        try:
            print("开始扫描串口...")
            serials = serial_scan()
            for port in serials:
                self.devices.add(port.device)

            print(self.devices)
            self.state = 1
        except:
            print("扫描串口失败")
            self.state = 0

        # 发射工作完成信号
        self.work_finished.emit()

