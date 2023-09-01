# -*- coding: utf-8 -*-            
# @Time : 2023/8/28 17:27
# @Author : IoT_H2
# @FileName: KEY.py
# @Software: PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog, QAction
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel


import serial
# from UI import KeySet


# class KEYSET(QMainWindow,KeySet.Ui_MainWindow):
#     def __init__(self,layout):
#         super(KEYSET, self).__init__()
#         self.setupUi(self)
#
#         self.label_6.setText("当前操作层：{}".format(layout))

class KEY():
    def __init__(self,KEYMODE="01",ID="00",FunCode1 = "00",FunCode2 = "00",FunCode3 = "00",FunCode4 = "00",FunCode5 = "00",KeyLayout = "02"):
        self.KeyMode = KEYMODE
        self.id = ID
        self.Funcode1 = FunCode1
        self.Funcode2 = FunCode2
        self.Funcode3 = FunCode3
        self.Funcode4 = FunCode4
        self.Funcode5 = FunCode5
        self.Endcode = "FF"
        self.KeyLayout = KeyLayout

        # self.Keyset = KEYSET(KeyLayout)
        # self.Keyset.label_6.setText("当前操作层：{}".format(self.KeyLayout))
        #
        # # 保存
        # self.Keyset.pushButton_ok.clicked.connect(self.ok)
        # # 取消，返回
        # self.Keyset.pushButton_ok.clicked.connect(self.Keyset.hide)

    def ok(self):
        self.Funcode1 = self.Keyset.lineEdit_1.text()
        self.Funcode2 = self.Keyset.lineEdit_2.text()
        self.Funcode3 = self.Keyset.lineEdit_3.text()
        self.Funcode4 = self.Keyset.lineEdit_4.text()
        self.Funcode5 = self.Keyset.lineEdit_5.text()

        self.Keyset.hide()



class KEYS_Matrix():
    def __init__(self,matrix = [[9,6,3],[2,5,8],[7,4,1]],config_dict = []):
        self.KEYS = [[0,0,0],[0,0,0],[0,0,0]]
        self.matrix = matrix
        num = 0
        for i in range(3):
            for j in range(3):
                id = str(matrix[i][j] - 1)
                if len(id) < 2:
                    id = "0" + id

                self.KEYS[i][j] = KEY(ID=id,FunCode1="{}".format(str(hex(49+num))[2:]))
                num += 1

    def show(self):
        print("------------------------------------------------------")
        for i in self.matrix:
            print(i)
        for i in self.KEYS:
            for j in i:
                print("id {} fun1 {} fun2 {} fun3 {} fun4 {} fun5 {}".format(j.id,j.Funcode1,j.Funcode2,j.Funcode3,j.Funcode4,j.Funcode5))
