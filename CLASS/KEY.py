# -*- coding: utf-8 -*-            
# @Time : 2023/8/28 17:27
# @Author : IoT_H2
# @FileName: KEY.py
# @Software: PyCharm

import serial

class KEY:
    def __init__(self,matrix = [[9,6,3],[2,5,8],[7,4,1]],KEYMODE="00",ID="00",FunCode1 = "00",FunCode2 = "00",FunCode3 = "00",FunCode4 = "00",FunCode5 = "00"):
        self.matrix = matrix
        self.KeyMode = KEYMODE
        self.id = ID
        self.Funcode1 = FunCode1
        self.Funcode2 = FunCode2
        self.Funcode3 = FunCode3
        self.Funcode4 = FunCode4
        self.Funcode5 = FunCode5









