# -*- coding: utf-8 -*-            
# @Time : 2023/8/28 15:37
# @Author : IoT_H2
# @FileName: main.py.py
# @Software: PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog, QAction
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPalette, QColor

from CLASS.THREAD import OpenSerialThread,ScanSerialThread


from UI import start, KeyLayout, Color_Palette



class START(QMainWindow,start.Ui_MainWindow):
    def __init__(self):
        self.matrix = {
            "up": [[7,8,9],[4,5,6],[1,2,3]],

            "left": [[9,6,3],[2,5,8],[7,4,1]],

            "right": [[1,4,7],[2,5,8],[3,6,9]],

            "down": [[3,2,1],[4,5,6],[9,8,7]]
            }

        super(START, self).__init__()
        self.setupUi(self)

        # 方向矩阵选择
        self.pushButton.clicked.connect(lambda: {self.hide(), KEYLAYOUT(self.matrix["up"]).show()})
        self.pushButton_2.clicked.connect(lambda: {self.hide(), KEYLAYOUT(self.matrix["left"]).show()})
        self.pushButton_3.clicked.connect(lambda: {self.hide(), KEYLAYOUT(self.matrix["right"]).show()})
        self.pushButton_4.clicked.connect(lambda: {self.hide(), KEYLAYOUT(self.matrix["down"]).show()})



class KEYLAYOUT(QMainWindow, KeyLayout.Ui_MainWindow):
    def __init__(self,matrix):
        # 首部
        Header = "4C"

        self.LightMode = "00"


        # RGB颜色报文
        self.RGB = 0

        print(matrix)

        super(KEYLAYOUT, self).__init__()
        self.setupUi(self)

        self.pushButton_close.hide() # 隐藏 关闭串口 按键
        self.pushButton_close.clicked.connect(lambda: {self.pushButton_close.hide(),
                                                      self.OpenSerial.ser.close(),
                                                      self.pushButton_open.show(),
                                                      self.label_LinkState.setText("串口已关闭")})

        # 返回方向矩阵选择
        self.pushButton_back.clicked.connect(lambda: {self.hide(),
                                                      START().show()})
        # 扫描 和 连接
        self.pushButton_scan.clicked.connect(lambda: {self.start_scan()}) # 扫描串口
        self.pushButton_open.clicked.connect(lambda: {self.start_connect(self.comboBox_2.currentText())}) #打开串口


        # RGB调色滑块
        self.Slider_R.valueChanged.connect(self.update_color)
        self.Slider_G.valueChanged.connect(self.update_color)
        self.Slider_B.valueChanged.connect(self.update_color)

        # combox1 模式选择
        self.comboBox.currentIndexChanged.connect(self.update_light_mode)
        self.update_light_mode()


    # 开始扫描
    def start_scan(self):
        print("扫描中...")
        self.ScanSerial = ScanSerialThread()
        self.ScanSerial.start()
        self.ScanSerial.work_finished.connect(self.scan_finished)

    # 扫描结束
    def scan_finished(self):
        if self.ScanSerial.state == 1:
            self.label_LinkState.setText("扫描成功")
            devices = list(self.ScanSerial.devices)
            self.comboBox_2.addItems(devices)
        else:
            self.label_LinkState.setText("扫描失败")


    # 开始连接
    def start_connect(self,COM = "COM6"):
        print("连接中...")
        self.OpenSerial = OpenSerialThread(COM)
        self.OpenSerial.start()
        self.OpenSerial.work_finished.connect(self.connect_finished)

    # 连接结束
    def connect_finished(self):
        if self.OpenSerial.state == 1:
            self.label_LinkState.setText("连接成功")
            self.pushButton_open.hide()
            self.pushButton_close.show()
        else:
            self.label_LinkState.setText("连接失败")

    # 颜色更新函数
    def update_color(self):
        red = self.Slider_R.value()
        green = self.Slider_G.value()
        blue = self.Slider_B.value()

        red = str(hex(red)).upper()[2:]
        green = str(hex(green)).upper()[2:]
        blue = str(hex(blue)).upper()[2:]

        if len(red) < 2:
            red = "0" + red
        if len(green) < 2:
            green = "0" + green
        if len(blue) < 2:
            blue = "0" + blue

        # 更新颜色
        self.RGB = red + green + blue
        self.Canvas.setStyleSheet("background-color: #{}{}{};".format(red,green,blue))

    def update_light_mode(self):
        # 非全局单色逻辑
        if self.comboBox.currentText() != "全局单色":
            self.Slider_R.hide()
            self.Slider_G.hide()
            self.Slider_B.hide()
            self.Canvas.hide()
            if self.comboBox.currentText() == "全局渐变":
                self.LightMode = "01"
            if self.comboBox.currentText() == "阶梯渐变":
                self.LightMode = "02"
            if self.comboBox.currentText() == "单颗渐变":
                self.LightMode = "03"
        # 全局单色逻辑
        else:
            self.Slider_R.show()
            self.Slider_G.show()
            self.Slider_B.show()
            self.Canvas.show()
            self.LightMode = "00"

    def UPDATE(self):
        self.update_light_mode()
        self.update_color()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = START()
    main.show()
    sys.exit(app.exec_())