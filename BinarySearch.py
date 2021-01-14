#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:16:25 2021

@author: hassan
"""
#here i used for
def binarySearch(seq,item):
    n = len(seq)
    for i in range(n):
        ind = (n+i)//2
        if seq[ind] == item:
            return True
        elif seq[ind] > item:
            n = ind - 1
        elif seq[ind] < item:
            i = ind + 1
    return False

print(binarySearch([1,2,3,4,5,6,7,8,9,10],2))

#here i used while to loop
def binarySearch1(seq,item):
    low  = 0
    high = len(seq) - 1
    while low <= high:
        ind = (high+low)//2
        if seq[ind] == item:
            return True
        elif seq[ind] > item:
            high = ind - 1
        elif seq[ind] < item:
            low = ind + 1
    return False

print(binarySearch1([1,2,3,4,5,6,7,8,9,10],0))