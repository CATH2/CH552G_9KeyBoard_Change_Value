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
        self.pushButton.setGeometry(QtCore.QRect(50, 30, 80, 80))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 30, 80, 80))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 30, 80, 80))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 130, 80, 80))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 130, 80, 80))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(250, 130, 80, 80))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 230, 80, 80))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(150, 230, 80, 80))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(250, 230, 80, 80))
        self.pushButton_9.setObjectName("pushButton_9")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(500, 50, 111, 28))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_open = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open.setGeometry(QtCore.QRect(190, 360, 93, 28))
        self.pushButton_open.setObjectName("pushButton_open")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(60, 360, 111, 28))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(450, 360, 93, 28))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(570, 360, 93, 28))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_RGB = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_RGB.setGeometry(QtCore.QRect(390, 50, 93, 28))
        self.pushButton_RGB.setObjectName("pushButton_RGB")
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(190, 360, 93, 28))
        self.pushButton_close.setObjectName("pushButton_close")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 703, 26))
        self.menubar.setObjectName("menubar")
        self.menuasd = QtWidgets.QMenu(self.menubar)
        self.menuasd.setObjectName("menuasd")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menuasd.addAction(self.action)
        self.menubar.addAction(self.menuasd.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_open.clicked.connect(self.pushButton_close.hide) # type: ignore
        self.pushButton_close.clicked.connect(self.pushButton_open.hide) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "设置"))
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
        self.pushButton_11.setText(_translate("MainWindow", "预览"))
        self.pushButton_save.setText(_translate("MainWindow", "保存更改"))
        self.pushButton_RGB.setText(_translate("MainWindow", "RGB调色盘"))
        self.pushButton_close.setText(_translate("MainWindow", "关闭串口"))
        self.menuasd.setTitle(_translate("MainWindow", "帮助"))
        self.action.setText(_translate("MainWindow", "联系作者"))