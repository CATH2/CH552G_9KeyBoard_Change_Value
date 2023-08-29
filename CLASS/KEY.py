# -*- coding: utf-8 -*-            
# @Time : 2023/8/28 17:27
# @Author : IoT_H2
# @FileName: KEY.py
# @Software: PyCharm

import serial

class KEY():
    def __init__(self,KEYMODE="00",ID="00",FunCode1 = "00",FunCode2 = "00",FunCode3 = "00",FunCode4 = "00",FunCode5 = "00"):
        self.KeyMode = KEYMODE
        self.id = ID
        self.Funcode1 = FunCode1
        self.Funcode2 = FunCode2
        self.Funcode3 = FunCode3
        self.Funcode4 = FunCode4
        self.Funcode5 = FunCode5

class KEYS_Matrix():
    def __init__(self,matrix = [[9,6,3],[2,5,8],[7,4,1]],):
        self.KEYS = [0,1,2,3,4,5,6,7,8]
        for i in range(3):
            for j in range(3):
                self.KEYS[i][j] = KEY(KEYMODE="00",ID="00",FunCode1 = "00",FunCode2 = "00",FunCode3 = "00",FunCode4 = "00",FunCode5 = "00")



















