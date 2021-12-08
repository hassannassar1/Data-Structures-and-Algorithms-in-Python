#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 15:52:00 2021

@author: hassan
"""

def rec_sum(arr):
    if len(arr) ==1:
        return arr[0]
    return arr[0]+rec_sum(arr[1:])
print (rec_sum([1, 2, 3, 4]))

def quicksort(li):
    if len(li) < 2:
        return li
    pivot = li[0]
    less = [i for i in li[1:] if i <= pivot]
    greater = [i for i in li[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10, 5, 2,19,20,0,3]))