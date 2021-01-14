#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:36:52 2021

@author: hassan
"""

def bubbleSort(seq):
    n = len(seq)
    for i in range(n-1):
        for j in range(n-i-1):
            if seq[j] > seq[j + 1] :
                tmp = seq[j]
                seq[j] = seq[j + 1]
                seq[j + 1] = tmp
ss= [10,1,2,5,4,7]  
bubbleSort(ss)
print(ss)