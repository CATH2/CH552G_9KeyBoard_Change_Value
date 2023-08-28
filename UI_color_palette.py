# -*- coding: utf-8 -*-
# @Time : 2023/8/28 17:58
# @Author : IoT_H2
# @FileName: UI_color_palette.py.py
# @Software: PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSlider,QWidget
from PyQt5.QtGui import QColor, QPainter, QPalette
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RGB调色盘")
        self.setGeometry(100, 100, 500, 500)  # 设置窗口大小和位置

        with open("config.json", "r") as f:
            # 记录文件中保存的RGB拖动条位置
            config = eval(f.read())

            # 创建滑动条
            self.red_slider = QSlider(Qt.Horizontal, self)
            self.blue_slider.setRange(0,255)
            self.red_slider.setSliderPosition(int(config["R"]))
            self.red_slider.valueChanged.connect(self.update_color)

            self.green_slider = QSlider(Qt.Horizontal, self)
            self.blue_slider.setRange(0,255)
            self.green_slider.setSliderPosition(int(config["G"]))
            self.green_slider.valueChanged.connect(self.update_color)

            self.blue_slider = QSlider(Qt.Horizontal, self)
            self.blue_slider.setRange(0,255)
            self.blue_slider.setSliderPosition(int(config["B"]))
            self.blue_slider.valueChanged.connect(self.update_color)
            f.close()

        # 创建垂直布局并将滑动条添加进去
        layout = QVBoxLayout()
        layout.addWidget(self.red_slider)
        layout.addWidget(self.green_slider)
        layout.addWidget(self.blue_slider)

        # 创建一个透明的画布用于显示颜色
        self.color_canvas = ColorCanvas(self)
        layout.addWidget(self.color_canvas)

        # 创建主窗口并设置布局
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 初始化颜色
        self.update_color()

    def update_color(self):
        # 获取滑动条当前值
        red = self.red_slider.value()
        green = self.green_slider.value()
        blue = self.blue_slider.value()

        R = red
        G = green
        B = blue

        # 创建颜色
        color = QColor(red, green, blue)


        red = str(hex(red)).upper()[2:]
        green = str(hex(green)).upper()[2:]
        blue = str(hex(blue)).upper()[2:]

        if len(red) < 2:
            red = "0" + red
        if len(green) < 2:
            green = "0" + green
        if len(blue) < 2:
            blue = "0" + blue

        RGB = red+green+blue
        with open("config.json","r") as f:
            config = eval(f.read())
            f.close()

        with open("config.json","w") as f:
            config["RGB"] = RGB
            config["R"] = R
            config["G"] = G
            config["B"] = B
            f.write(str(config))

            f.close()

        # 根据颜色更新画布
        self.color_canvas.set_color(color)
        self.color_canvas.update()


class ColorCanvas(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        # 设置画布大小
        self.setMinimumSize(200, 200)

        # 初始化颜色为白色
        self.color = QColor(Qt.white)

    def set_color(self, color):
        self.color = color

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), self.color)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
