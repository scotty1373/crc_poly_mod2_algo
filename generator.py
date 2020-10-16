#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def get_bit_val(byte, index):
    if byte & (1 << index):
        return 1
    else:
        return 0

def crc12_ploy(min, max):
    a, b = 0, 0
    i = 0
    f = open("crc_poly_data.txt", "a")
    for x in range(min,max):
        b = '{:013b}' .format(x)
        i = int(b)
        if get_bit_val(i, 0)==1:
            f.write(b)
            f.write("\r\n")
        else:
            pass   
        a = a + 1
    return 'done'
    f.close()

crc12_ploy(4096,8192)   
 

