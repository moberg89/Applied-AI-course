# -*- coding: utf-8 -*-
"""
will be something more
"""
import numpy
#data=[(1,1.5),(3,3), (3.03453337734,3.35677421955)]

data=[(4,4)]
minnum=-10
maxnum=10
for i in range(10):
    a=(maxnum-minnum)*numpy.random.random_sample()+minnum    
    b=(maxnum-minnum)*numpy.random.random_sample()+minnum
    data.append((a,b))
i=numpy.linspace(0,2*numpy.pi, 100)
for j in i:
    p=(10*numpy.cos(j), 10*numpy.sin(j))
    data.append(p)

def read_sensors(current_pos, current_ori):
    return data 