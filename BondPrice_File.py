#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 09:45:55 2024

@author: yiyangxu
"""

import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    
    C=(couponRate*face)/ppy
    n=m*ppy
    i=y/ppy
    t=np.arange(1,n+1)
    pvc=C*np.sum(1/(1+i)**t)
    pvf=face/(1+i)**n
    price=pvc+pvf
    
    return(price)


# Test values

y = 0.03
face = 2000000
couponRate = 0.04
m = 10
