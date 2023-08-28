# -*- coding: utf-8 -*-            
# @Time : 2023/8/28 17:49
# @Author : IoT_H2
# @FileName: function_serial.py
# @Software: PyCharm

import serial
import serial.tools.list_ports


# 串口扫描
def serial_scan():
    serials = []
    # 扫描可用的串口号
    available_ports = serial.tools.list_ports.comports()

    # 打印可用的串口号
    for port in available_ports:
        serials.append(port)
        print(port.device)

    return

if __name__ == '__main__':
    serial_scan()
