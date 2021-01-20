#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 16:32:11 2021

@author: hassan
"""

def fact(n):
    assert n >= 0, "Factorial not defined for negative values."
    if n < 2:
        return 1
    return fact(n-1) * n
fact(6)

def fib( n ):
    if  n < 0:
        return"Fibonacci not defined for n < 1."
    if n ==0 :
        return 0
    elif n ==1 :
        return 1
    else :
        return fib(n-1) + fib(n-2)

fib(9)
fib(-2)

