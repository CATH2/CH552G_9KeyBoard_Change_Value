# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\KeyLayout.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(703, 476)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 50, 80, 80))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 50, 80, 80))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 50, 80, 80))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 150, 80, 80))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 150, 80, 80))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(250, 150, 80, 80))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 250, 80, 80))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(150, 250, 80, 80))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(250, 250, 80, 80))
        self.pushButton_9.setObjectName("pushButton_9")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(510, 60, 111, 28))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_open = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open.setGeometry(QtCore.QRect(190, 380, 93, 28))
        self.pushButton_open.setObjectName("pushButton_open")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(50, 380, 121, 28))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_preview = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_preview.setGeometry(QtCore.QRect(450, 360, 93, 28))
        self.pushButton_preview.setObjectName("pushButton_preview")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(570, 360, 93, 28))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(190, 380, 93, 28))
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(10, 10, 101, 28))
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_scan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_scan.setGeometry(QtCore.QRect(190, 350, 93, 28))
        self.pushButton_scan.setObjectName("pushButton_scan")
        self.label_LinkState = QtWidgets.QLabel(self.centralwidget)
        self.label_LinkState.setGeometry(QtCore.QRect(61, 350, 101, 20))
        self.label_LinkState.setText("")
        self.label_LinkState.setObjectName("label_LinkState")
        self.Canvas = QtWidgets.QTextBrowser(self.centralwidget)
        self.Canvas.setGeometry(QtCore.QRect(420, 40, 81, 51))
        self.Canvas.setObjectName("Canvas")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(420, 90, 271, 176))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Slider_R = QtWidgets.QSlider(self.layoutWidget)
        self.Slider_R.setMaximum(255)
        self.Slider_R.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_R.setObjectName("Slider_R")
        self.verticalLayout.addWidget(self.Slider_R)
        self.Slider_G = QtWidgets.QSlider(self.layoutWidget)
        self.Slider_G.setMaximum(255)
        self.Slider_G.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_G.setObjectName("Slider_G")
        self.verticalLayout.addWidget(self.Slider_G)
        self.Slider_B = QtWidgets.QSlider(self.layoutWidget)
        self.Slider_B.setMaximum(255)
        self.Slider_B.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_B.setObjectName("Slider_B")
        self.verticalLayout.addWidget(self.Slider_B)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(510, 30, 111, 28))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton_view = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_view.setGeometry(QtCore.QRect(100, 100, 80, 80))
        self.pushButton_view.setObjectName("pushButton_view")
        self.label_Now_Layout = QtWidgets.QLabel(self.centralwidget)
        self.label_Now_Layout.setGeometry(QtCore.QRect(290, 30, 111, 21))
        self.label_Now_Layout.setObjectName("label_Now_Layout")
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(250, 350, 195, 31))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_Yes = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_Yes.setObjectName("pushButton_Yes")
        self.horizontalLayout_4.addWidget(self.pushButton_Yes)
        self.pushButton_Cancel = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.horizontalLayout_4.addWidget(self.pushButton_Cancel)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(300, 70, 101, 231))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_fun1 = QtWidgets.QLabel(self.widget)
        self.label_fun1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_fun1.setObjectName("label_fun1")
        self.verticalLayout_2.addWidget(self.label_fun1)
        self.label_fun2 = QtWidgets.QLabel(self.widget)
        self.label_fun2.setObjectName("label_fun2")
        self.verticalLayout_2.addWidget(self.label_fun2)
        self.label_fun3 = QtWidgets.QLabel(self.widget)
        self.label_fun3.setObjectName("label_fun3")
        self.verticalLayout_2.addWidget(self.label_fun3)
        self.label_fun4 = QtWidgets.QLabel(self.widget)
        self.label_fun4.setObjectName("label_fun4")
        self.verticalLayout_2.addWidget(self.label_fun4)
        self.label_fun5 = QtWidgets.QLabel(self.widget)
        self.label_fun5.setObjectName("label_fun5")
        self.verticalLayout_2.addWidget(self.label_fun5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_fun1 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_fun1.setObjectName("lineEdit_fun1")
        self.verticalLayout_3.addWidget(self.lineEdit_fun1)
        self.lineEdit_fun2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_fun2.setObjectName("lineEdit_fun2")
        self.verticalLayout_3.addWidget(self.lineEdit_fun2)
        self.lineEdit_fun3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_fun3.setObjectName("lineEdit_fun3")
        self.verticalLayout_3.addWidget(self.lineEdit_fun3)
        self.lineEdit_fun4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_fun4.setObjectName("lineEdit_fun4")
        self.verticalLayout_3.addWidget(self.lineEdit_fun4)
        self.lineEdit_fun5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_fun5.setObjectName("lineEdit_fun5")
        self.verticalLayout_3.addWidget(self.lineEdit_fun5)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 703, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CH552G改键 v0.9 改键版"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.pushButton_2.setText(_translate("MainWindow", "+"))
        self.pushButton_3.setText(_translate("MainWindow", "+"))
        self.pushButton_4.setText(_translate("MainWindow", "+"))
        self.pushButton_5.setText(_translate("MainWindow", "+"))
        self.pushButton_6.setText(_translate("MainWindow", "+"))
        self.pushButton_7.setText(_translate("MainWindow", "+"))
        self.pushButton_8.setText(_translate("MainWindow", "+"))
        self.pushButton_9.setText(_translate("MainWindow", "+"))
        self.comboBox.setItemText(0, _translate("MainWindow", "全局单色"))
        self.comboBox.setItemText(1, _translate("MainWindow", "全局渐变"))
        self.comboBox.setItemText(2, _translate("MainWindow", "阶梯渐变"))
        self.comboBox.setItemText(3, _translate("MainWindow", "单颗渐变"))
        self.pushButton_open.setText(_translate("MainWindow", "打开串口"))
        self.pushButton_preview.setText(_translate("MainWindow", "预览"))
        self.pushButton_save.setText(_translate("MainWindow", "保存更改"))
        self.pushButton_close.setText(_translate("MainWindow", "关闭串口"))
        self.pushButton_back.setText(_translate("MainWindow", "返回方向调整"))
        self.pushButton_scan.setText(_translate("MainWindow", "扫描串口"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "自定义"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "数字层"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "鼠标层"))
        self.pushButton_view.setText(_translate("MainWindow", "+"))
        self.label_Now_Layout.setText(_translate("MainWindow", "当前层:"))
        self.pushButton_Yes.setText(_translate("MainWindow", "确定"))
        self.pushButton_Cancel.setText(_translate("MainWindow", "取消"))
        self.label_fun1.setText(_translate("MainWindow", "功能1"))
        self.label_fun2.setText(_translate("MainWindow", "功能2"))
        self.label_fun3.setText(_translate("MainWindow", "功能3"))
        self.label_fun4.setText(_translate("MainWindow", "功能4"))
        self.label_fun5.setText(_translate("MainWindow", "功能5"))
        self.menu.setTitle(_translate("MainWindow", "帮助"))
        self.action.setText(_translate("MainWindow", "联系作者"))
        self.action_2.setText(_translate("MainWindow", "环境搭建"))
        self.action_3.setText(_translate("MainWindow", "开源地址"))
