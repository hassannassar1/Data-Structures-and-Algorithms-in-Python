#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 12:38:09 2021

@author: hassan
"""

def binary_search(n,li):
    low = 0
    hi = len(li)-1
    while low <= hi:
        ind = (hi+low)//2
        if n == li[ind]:
            return ind
        elif n>li[ind]:
            low = ind + 1
        else:
            hi = ind - 1
    return -1

binary_search(10,[2,3,4,5,6,7,8,9,10])

def rec_binary_search(n, li, low, hi):
    if low > hi:
        return -1 
    
    ind = (hi + low) // 2
    if li[ind] == n:
        return ind
    elif li[ind] > n:
        return rec_binary_search(n, li, low, ind - 1)
    else:
        return rec_binary_search(n, li, ind + 1, hi)
              
li = [2,3,4,5,6,7,8,9,10]
print(rec_binary_search(11,li,0,len(li)-1))