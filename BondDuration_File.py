#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 09:57:54 2024

@author: yiyangxu
"""
import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    
    C=(couponRate*face)/ppy
    n=m*ppy
    i=y/ppy
    t=np.arange(1,n+1)
    cash_flows=np.full(n, C)
    cash_flows[-1]+=face
    pv_cf=cash_flows/(1+i)**t
    bond_price=np.sum(pv_cf)
    weights=pv_cf/bond_price
    bondDuration=np.sum(weights*t)
    
    return(bondDuration)



# Test values

y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1