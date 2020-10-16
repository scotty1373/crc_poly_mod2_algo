# -*- coding: utf-8 -*-
import numpy as np
def crc_cal(info, crc_poly_bit12):
    data =  info
    crc_length = 12
    times = len(info)

    count = 0
    p = [0 for i in range(12)]                          #左起为第一位
    for i in crc_poly_bit12:                            #生成式int化
        if i == '1':
            p[count] = 1
        count = count + 1
    #crc_poly_bit12 = crc_poly_bit12[::-1]
    
    # 左移补零
    for i in range(crc_length-1):                        #数据位补0
        data.append(0)
    # 除
    divisor = []
    for i in range(times):                               #位数选择
        if data[i] == 1:
            divisor.append(1)                            #当数据位为1，商就添1
            for j in range(crc_length):                  #数据与多项式异或
                data[j + i] = data[j + i] ^ p[j]
        else:
            divisor.append(0)                            #最后一位开始循环，数据为0商就添0
    # 余数
    remainder = data[-(crc_length-1)::]                  #数组切片，到余数位个时截止
    return remainder

# 随机数据

crc_poly_data = open("crc_poly_data.txt","r")
crc_poly_data.seek(0,0)
rand_data = open("rand_data.txt","r")
rand_data.seek(0,0)

for i in range(2047):
    k_num = str(i)
    file_name = 'data_remainder' + k_num
    crc_remainder = open(file_name, "a")
    poly_code = list(crc_poly_data.read(12))
    rand_data.seek(0,0)                                  #重置rand_data文件 offset
    for rand_times in range(2000):
        m = rand_data.read(60)
        count = 0
        data = [0 for i in range(60)]
        for i in m:                                      #数据int化
            if i == '1':
                data[count] = 1
            count = count + 1
        data = list(data)
        data_copy = data.copy()                             #data list进函数之前重新赋值
        poly_code_copy = poly_code.copy()                   #poly list进函数之前重新赋值
        crc = crc_cal(data_copy,poly_code_copy)
        crc_remainder.write(''.join([str(j) for j in crc]))
        crc_remainder.write("\r\n")
        #print('{:12}\t{}'.format('余数：', crc))
    crc_remainder.close()
crc_poly_data.close()










