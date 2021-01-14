#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:53:53 2021

@author: hassan
"""

def linearSearch(seq,item):
    for i in range(len(seq)):
        if item == seq[i]:
            return True
    return False

print(linearSearch([5,8,2,4,10],11))