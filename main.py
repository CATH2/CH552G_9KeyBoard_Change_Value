# -*- coding: utf-8 -*-            
# @Time : 2023/8/28 15:37
# @Author : IoT_H2
# @FileName: main.py.py
# @Software: PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog, QAction
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPalette, QColor

import functools



from UI import start, KeyLayout,KeySet
from CLASS.KEY import KEY, KEYS_Matrix
from CLASS.THREAD import OpenSerialThread,ScanSerialThread,SendSerialThread,FileWriteThread




class START(QMainWindow,start.Ui_MainWindow):
    def __init__(self):
        self.matrix = {
            "up": [[7,8,9],[4,5,6],[1,2,3]],

            "left": [[9,6,3],[8,5,2],[7,4,1]],

            "right": [[1,4,7],[2,5,8],[3,6,9]],

            "down": [[3,2,1],[6,5,4],[9,8,7]]
            }

        super(START, self).__init__()
        self.setupUi(self)

        WINDOW2 = KEYLAYOUT(self.matrix["left"],"left")

        # 方向矩阵选择
        self.pushButton.clicked.connect(lambda: {self.close(), WINDOW2.__init__(self.matrix["up"],"up"),WINDOW2.show()})
        self.pushButton_2.clicked.connect(lambda: {self.hide(), WINDOW2.__init__(self.matrix["left"],"left"),WINDOW2.show()})
        self.pushButton_3.clicked.connect(lambda: {self.hide(), WINDOW2.__init__(self.matrix["right"],"right"), WINDOW2.show()})
        self.pushButton_4.clicked.connect(lambda: {self.hide(), WINDOW2.__init__(self.matrix["down"],"down"), WINDOW2.show()})

        self.action.triggered.connect(lambda :{self.GoURL("https://blog.csdn.net/qq_53381910?spm=1000.2115.3001.5343")})

    def GoURL(self, url):
        import webbrowser
        webbrowser.open(url)



class KEYLAYOUT(QMainWindow, KeyLayout.Ui_MainWindow):
    def __init__(self,matrix,diretion):
        super(KEYLAYOUT, self).__init__()
        self.setupUi(self)

        # 刷新
        self.UPDATE()

        # 首部
        self.Header = "4C"
        # 不知道是啥，先定成按键层吧
        self.Layout = "02"
        # 灯光模式
        self.LightMode = "00"
        # RGB颜色
        self.RGB = "000000"

        # 按键类初始化
        # 读取之前的配置
        self.diretion = diretion
        self.matrix = matrix

        with open("keyconfig.json", "r") as f:
            KEY_VALUES = eval(f.read())
            print()
            f.close()
        with open("test.json","r+") as f:
            self.keyconfig = eval(f.read())



        self.KEYS = KEYS_Matrix(matrix,KEY_VALUES[self.diretion])

        # 串口初始化，防止报错
        self.SER = 0

        # print(matrix)


        self.StopSetKey()

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

        # 键盘层选择
        self.comboBox_3.currentIndexChanged.connect(self.update_layout_mode)

        # 预览
        self.pushButton_preview.clicked.connect(self.Preview)
        # 下载
        self.pushButton_save.clicked.connect(self.Download)

        """界面3"""
        # 编辑按键
        # functools.partial(mySlot, arg1, arg2)

        self.pushButton.clicked.connect(lambda :{self.StartSetKey(0, 0)})
        self.pushButton_2.clicked.connect(lambda: {self.StartSetKey(0, 1)})
        self.pushButton_3.clicked.connect(lambda: {self.StartSetKey(0, 2)})
        self.pushButton_4.clicked.connect(lambda: {self.StartSetKey(1, 0)})
        self.pushButton_5.clicked.connect(lambda: {self.StartSetKey(1, 1)})
        self.pushButton_6.clicked.connect(lambda: {self.StartSetKey(1, 2)})
        self.pushButton_7.clicked.connect(lambda: {self.StartSetKey(2, 0)})
        self.pushButton_8.clicked.connect(lambda: {self.StartSetKey(2, 1)})
        self.pushButton_9.clicked.connect(lambda: {self.StartSetKey(2, 2)})


        self.pushButton_Cancel.clicked.connect(lambda :{self.SetKeyNO()})


        # 帮助
        self.action.triggered.connect(lambda :{self.GoURL("https://blog.csdn.net/qq_53381910?spm=1000.2115.3001.5343")})
        self.action_2.triggered.connect(lambda: {self.GoURL("https://blog.csdn.net/qq_53381910/article/details/132516628?spm=1001.2014.3001.5501")})
        self.action_3.triggered.connect(lambda: {self.GoURL("https://oshwhub.com/lh118/136")})

    def StartSetKey(self,i,j):
        # 界面1 按钮隐藏
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        self.pushButton_5.hide()
        self.pushButton_6.hide()
        self.pushButton_7.hide()
        self.pushButton_8.hide()
        self.pushButton_9.hide()
        self.pushButton_back.hide()
        self.pushButton_save.hide()
        self.pushButton_preview.hide()
        self.pushButton_scan.hide()
        self.pushButton_open.hide()
        self.pushButton_close.hide()

        self.comboBox.hide()
        self.comboBox_2.hide()
        self.comboBox_3.hide()

        self.Slider_R.hide()
        self.Slider_G.hide()
        self.Slider_B.hide()

        self.Canvas.hide()

        # 界面2 按钮显示
        self.pushButton_view.show()

        self.pushButton_Cancel.show()
        self.pushButton_Yes.show()

        self.label_fun1.show()
        self.label_fun2.show()
        self.label_fun3.show()
        self.label_fun4.show()
        self.label_fun5.show()

        Layout = self.Layout
        if Layout == "02":
            self.label_Now_Layout.setText("当前层:{}".format("自定义"))
        if Layout == "00":
            self.label_Now_Layout.setText("当前层:{}".format("数字层"))
        if Layout == "01":
            self.label_Now_Layout.setText("当前层:{}".format("鼠标层"))
        self.label_Now_Layout.show()

        self.lineEdit_fun1.setText("")
        self.lineEdit_fun1.show()
        self.lineEdit_fun2.setText("")
        self.lineEdit_fun2.show()
        self.lineEdit_fun3.setText("")
        self.lineEdit_fun3.show()
        self.lineEdit_fun4.setText("")
        self.lineEdit_fun4.show()
        self.lineEdit_fun5.setText("")
        self.lineEdit_fun5.show()

        self.pushButton_Yes.clicked.connect(lambda: {self.SetKeyOK(i, j)})
        self.lineEdit_fun1.setText(self.keyconfig[self.diretion][self.KEYS.KEYS[i][j].id]["FunCode1"])
        self.lineEdit_fun2.setText(self.keyconfig[self.diretion][self.KEYS.KEYS[i][j].id]["FunCode2"])
        self.lineEdit_fun3.setText(self.keyconfig[self.diretion][self.KEYS.KEYS[i][j].id]["FunCode3"])
        self.lineEdit_fun4.setText(self.keyconfig[self.diretion][self.KEYS.KEYS[i][j].id]["FunCode4"])
        self.lineEdit_fun5.setText(self.keyconfig[self.diretion][self.KEYS.KEYS[i][j].id]["FunCode5"])




    def StopSetKey(self):
        # 界面1 按钮显示
        self.pushButton.show()
        self.pushButton_2.show()
        self.pushButton_3.show()
        self.pushButton_4.show()
        self.pushButton_5.show()
        self.pushButton_6.show()
        self.pushButton_7.show()
        self.pushButton_8.show()
        self.pushButton_9.show()
        self.pushButton_back.show()
        self.pushButton_save.show()
        self.pushButton_preview.show()
        self.pushButton_scan.show()
        self.pushButton_open.show()

        self.comboBox.show()
        self.comboBox_2.show()
        self.comboBox_3.show()

        self.Slider_R.show()
        self.Slider_G.show()
        self.Slider_B.show()

        self.Canvas.show()

        # 界面2 按钮隐藏
        self.pushButton_view.hide()
        self.pushButton_Cancel.hide()
        self.pushButton_Yes.hide()

        self.label_fun1.hide()
        self.label_fun2.hide()
        self.label_fun3.hide()
        self.label_fun4.hide()
        self.label_fun5.hide()

        self.label_Now_Layout.hide()

        self.lineEdit_fun1.hide()
        self.lineEdit_fun2.hide()
        self.lineEdit_fun3.hide()
        self.lineEdit_fun4.hide()
        self.lineEdit_fun5.hide()

    def SetKeyOK(self,a,b):
        def add_0(s):
            if s == "":
                s = "00"
            if len(s) < 2:
                s = "0" + s
            return s
        self.keyconfig[self.diretion][self.KEYS.KEYS[a][b].id]["FunCode1"]= add_0(self.lineEdit_fun1.text())
        self.KEYS.KEYS[a][b].Funcode1 = add_0(self.lineEdit_fun1.text())

        self.keyconfig[self.diretion][self.KEYS.KEYS[a][b].id]["FunCode2"]= add_0(self.lineEdit_fun2.text())
        self.KEYS.KEYS[a][b].Funcode2 = add_0(self.lineEdit_fun2.text())

        self.keyconfig[self.diretion][self.KEYS.KEYS[a][b].id]["FunCode3"]= add_0(self.lineEdit_fun3.text())
        self.KEYS.KEYS[a][b].Funcode3 = add_0(self.lineEdit_fun3.text())

        self.keyconfig[self.diretion][self.KEYS.KEYS[a][b].id]["FunCode4"]= add_0(self.lineEdit_fun4.text())
        self.KEYS.KEYS[a][b].Funcode4 = add_0(self.lineEdit_fun4.text())

        self.keyconfig[self.diretion][self.KEYS.KEYS[a][b].id]["FunCode5"]= add_0(self.lineEdit_fun5.text())
        self.KEYS.KEYS[a][b].Funcode5 = add_0(self.lineEdit_fun5.text())

        self.StopSetKey()
        self.KEYS.show()

        self.pushButton_Yes.clicked.disconnect()


    def start_write(self,filename,keyconfig):
        self.filewrite = FileWriteThread(filename,keyconfig)
        self.filewrite.start()

    def SetKeyNO(self):
        self.StopSetKey()

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
            self.SER = self.OpenSerial.ser
        else:
            self.label_LinkState.setText("连接失败")

    def start_send(self, SER, MESSAGE):
        if SER == 0:
            print("请先连接串口")
        else:
            print("发送中")
            self.SendSerial = SendSerialThread(SER, MESSAGE)
            self.SendSerial.start()
            self.SendSerial.work_finished.connect(self.send_finished)

            # keyconfig ={}
            # keyconfig[self.diretion] = {}

            print(self.KEYS.KEYS[2][2].Funcode1)

            print(self.keyconfig[self.diretion][self.KEYS.KEYS[2][2].id]["FunCode1"])

            self.filewrite = FileWriteThread("test.json", self.keyconfig)
            self.filewrite.start()



    def send_finished(self):
        self.label_LinkState.setText("       ")
        self.label_LinkState.setText("发送完成")



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
        # 更新背景板颜色
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

    def update_layout_mode(self):
        # 非自定义层
        if self.comboBox_3.currentText() != "自定义":
            if self.comboBox_3.currentText() == "数字层":
                self.Layout = "00"
            if self.comboBox_3.currentText() == "鼠标层":
                self.Layout = "01"
        # 自定义层
        else:
            self.Layout = "02"




    # 所有的更新函数都放这里吧
    def UPDATE(self):
        self.update_light_mode()
        self.update_color()


    # Preview 函数 和 Download 函数相同，只是结尾标志位不同
    def Preview(self):
        self.UPDATE()
        message = self.Header + self.Layout + self.LightMode + self.RGB
        # 3*3 键盘报文读取
        for i in range(3):
            for j in range(3):
                message += self.KEYS.KEYS[i][j].KeyMode + self.KEYS.KEYS[i][j].id + self.KEYS.KEYS[i][j].Funcode1 + self.KEYS.KEYS[i][j].Funcode2 + self.KEYS.KEYS[i][j].Funcode3 + self.KEYS.KEYS[i][j].Funcode4 + self.KEYS.KEYS[i][j].Funcode5 + self.KEYS.KEYS[i][j].Endcode


        if len(message) < 258:
            message = message + "F" * (258 - len(message))
        # message = self.add_F(message)
        message += "00"
        print(message)

        self.start_send(self.SER,message)


    # Download 函数 和 Preview 函数相同，只是结尾标志位不同
    def Download(self):
        self.UPDATE()
        message = self.Header + self.Layout + self.LightMode + self.RGB

        # 3*3 键盘报文读取
        for i in range(3):
            for j in range(3):
                message += self.KEYS.KEYS[i][j].KeyMode + self.KEYS.KEYS[i][j].id + self.KEYS.KEYS[i][j].Funcode1 + self.KEYS.KEYS[i][j].Funcode2 + self.KEYS.KEYS[i][j].Funcode3 + self.KEYS.KEYS[i][j].Funcode4 + self.KEYS.KEYS[i][j].Funcode5 + self.KEYS.KEYS[i][j].Endcode
                print(message)
        if len(message) < 258:
            message = message + "F" * (258 - len(message))
        message += "01"
        print(message)

        self.start_send(self.SER,message)

    def add_F(s):
        if len(s) < 260:
            s = s + "F" * (258 - len(s))
            # print(s)
        else:
            pass
            # print(s)
        return s

    def GoURL(self,url):
        import webbrowser
        webbrowser.open(url)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = START()
    main.show()
    sys.exit(app.exec_())