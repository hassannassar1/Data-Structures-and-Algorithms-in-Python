#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 18:04:53 2021

@author: hassan
"""

def selectionSort(seq):
    n = len(seq)
    for i in range( n - 1 ):
        smallest = i
        for j in range( i + 1, n ):
            if seq[j] < seq[smallest] :
                smallest = j
        if smallest != i :
            tmp = seq[i]
            seq[i] = seq[smallest]
            seq[smallest] = tmp

ss= [10,1,2,5,4,7]  
selectionSort(ss)
print(ss)