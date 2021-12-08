#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 17:06:23 2021

@author: hassan
"""
def fbes(h,w):
    if h == .5*w or w ==.5*h or h==w:
        return min(h,w)
    mi = min(h,w)
    ma = max(h,w)
    return fbes(mi,ma-mi)
fbes(6,9)