# -*- coding: utf-8 -*-            
# @Time : 2023/8/28 15:37
# @Author : IoT_H2
# @FileName: main.py.py
# @Software: PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog, QAction
from PyQt5 import QtCore, QtWidgets

from CLASS.THREAD import OpenSerialThread,ScanSerialThread,Fail_Connect


from UI import start
from UI import KeyLayout



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
    def __init__(self,matrix):

        print(matrix)

        super(KeyLayout, self).__init__()
        self.setupUi(self)

        self.pushButton_close.hide() # 隐藏 关闭串口


        self.pushButton_back.clicked.connect(lambda: {self.hide(), START().show()}) # 返回方向矩阵选择

        self.pushButton_scan.clicked.connect(lambda: {self.start_scan()}) # 扫描串口
        self.pushButton_open.clicked.connect(lambda: {self.start_connect(self.comboBox_2.currentText())}) #打开串口



    def start_scan(self):
        print("扫描中...")
        self.worker_thread = ScanSerialThread()
        self.worker_thread.start()
        self.worker_thread.work_finished.connect(self.scan_finished)

    def scan_finished(self):
        if self.worker_thread.state == 1:
            self.label_LinkState.setText("扫描成功")
            print(self.worker_thread.devices)
            self.comboBox_2.addItems(self.worker_thread.devices)
        else:
            self.label_LinkState.setText("扫描失败")

    def start_connect(self,COM = "COM6"):
        print("连接中...")
        self.worker_thread = OpenSerialThread(COM)
        self.worker_thread.start()
        self.worker_thread.work_finished.connect(self.connect_finished)

    def connect_finished(self):
        if self.worker_thread.state == 1:
            self.label_LinkState.setText("连接成功")
        else:
            self.label_LinkState.setText("连接失败")




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = START()
    main.show()
    sys.exit(app.exec_())


