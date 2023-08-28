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
        # print(port.device)

    return serials

# 打开串口
def serial_connect(COM):
    ser = serial.Serial(COM, 115200)  # 替换为您要连接的串口号和波特率
    return ser




if __name__ == '__main__':

    serial_scan()
    ser = serial_connect("COM5")
    ser.setDTR(True)

    while True:
    # 发送数据
        hex_data = "4C0200123f560100410000FF010142FF010243FF010344FF010445FF010546FF010647FF010748FF010849FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF01"
        ser.write(bytes.fromhex(hex_data))
    # 读取数据
        data = ser.read(10)  # 读取10个字节的数据
        print(data)
    # 关闭串口
    ser.close()
