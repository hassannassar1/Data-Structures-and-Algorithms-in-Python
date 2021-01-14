#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 18:31:46 2021

@author: hassan
"""

def insertionSort( seq ):
    n = len( seq )
    for i in range( 1, n ) :
        value = seq[i]
        pos = i
        while pos > 0 and value < seq[pos - 1] :
            seq[pos] = seq[pos - 1]
            pos -= 1
        seq[pos] = value

ss= [10,1,2,5,4,7]  
insertionSort(ss)
print(ss)