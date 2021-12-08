#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 18:59:09 2021

@author: hassan
"""

def mergeSortedLists(seq1,seq2):
    seq = list()
    a = 0
    b = 0
    while a < len(seq1) and b < len(seq2):
        if seq1[a] < seq1[b]:
            seq.append(seq1[a])
            a += 1
        elif seq1[b] < seq1[a]:
            seq.append(seq2[b])
            b += 1
        else:
            seq.append(seq1[a])
            seq.append(seq2[b])
            a += 1
            b += 1
    while a < len( listA ) :
        seq.append( seq1[a] )
        a += 1
    while b < len( listB ) :
        seq.append( seq2[b] )
        b += 1
    return seq
listA = [ 2, 8, 15, 23, 37 ]
listB = [ 4, 6, 15, 20 ]
newList = mergeSortedLists( listA, listB )
print( newList )