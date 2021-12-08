#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 20:54:59 2021

@author: hassan
"""
def pythonMergeSort( theList ):
    if len(theList) <= 1 :
        return theList
    else :
        mid = len(theList) // 2
        leftHalf = pythonMergeSort( theList[ :mid ] )
        rightHalf = pythonMergeSort( theList[ mid: ] )
        newList = mergeOrderedLists( leftHalf, rightHalf )
        return newList
    
def mergeOrderedLists( listA, listB ) :
    newList = list()
    a = 0
    b = 0
    while a < len( listA ) and b < len( listB ) :
        if listA[a] < listB[b] :
            newList.append( listA[a] )
            a += 1
        else :
            newList.append( listB[b] )
            b += 1
    while a < len( listA ) :
        newList.append( listA[a] )
        a += 1
    while b < len( listB ) :
        newList.append( listB[b] )
        b += 1
    return newList

#Advance the algorithm
def recMergeSort( theSeq, first, last, tmpArray ):
    if first == last :
        return;
    else :
        mid = (first + last) // 2
        recMergeSort( theSeq, first, mid, tmpArray )
        recMergeSort( theSeq, mid+1, last, tmpArray )
        mergeVirtualSeq( theSeq, first, mid+1, last+1, tmpArray )
def mergeVirtualSeq( theSeq, left, right, end, tmpArray ):
    a = left
    b = right
    m = 0
    while a < right and b < end :
        if theSeq[a] < theSeq[b] :
            tmpArray[m] = theSeq[a]
            a += 1
        else :
            tmpArray[m] = theSeq[b]
            b += 1
        m += 1
    while a < right :
        tmpArray[m] = theSeq[a]
        a += 1
        m += 1
    while b < end :
        tmpArray[m] = theSeq[b]
        b += 1
        m += 1
    for i in range( end - left ) :
        theSeq[i+left] = tmpArray[i]




a = [4,6,8,2,1,0,-1,10,20,15]
b = pythonMergeSort( a )