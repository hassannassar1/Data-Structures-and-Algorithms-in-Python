#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:42:54 2021

@author: hassan
"""
def findSmallest(li):
    smallest = li[0]
    smallest_index = 0
    for i in range(1, len(li)):
        if li[i] < smallest:
            smallest = li[i]
            smallest_index = i
    return smallest_index

def selection_sort(li):
    new_li = []
    for i in range(len(li)):
        smallest = findSmallest(li)
        new_li.append(li.pop(smallest))
    return new_li
    
print (selection_sort([5, 3, 6, 2, 10]))

def rec_selection_sort(li,new_li):
    if len(li) ==0:
        return -1
    smallest = findSmallest(li)
    new_li.append(li.pop(smallest))
    rec_selection_sort(li,new_li)
    return new_li
new_li = []    
print (rec_selection_sort([5, 3, 6,11, 2, 10,0],new_li))