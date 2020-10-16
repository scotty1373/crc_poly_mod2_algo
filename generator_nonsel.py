#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import numpy as np

def rand_data():
    f = open("rand_data.txt", "a")
    for x in range(2000):
        for k in range(100):
            m = np.random.randint(0,2,60)
            if m[0] == 1:
                m = ''.join([str(j) for j in m])
                break
            else:
                pass
        f.write(m)
    f.close()

rand_data()

 

