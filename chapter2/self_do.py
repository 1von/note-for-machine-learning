# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 01:58:50 2017

@author: 
"""
import os
os.chdir('os.chdir(u"F://coding//machine learn note//note-for-machine-learning//chapter2")')
from recommendations import critics
critics['Lisa Rose']

from math import pow,sqrt
import numpy as np 
def distance(data,p1,p2):
    dis=0
    for item in data[p1]:
        if item in data[p2]:
            dis+=(data[p1][item]-data[p2][item])**2
            
    d=1/(1+sqrt(dis))
    return d
distance(critics,'Lisa Rose','Gene Seymour')

def perason(data,p1,p2):
    a=[]
    b=[]
    for item in data[p1]:
        if item in data[p2]:
            a.append(data[p1][item])
            b.append(data[p2][item])
    p=np.corrcoef(a,b)
