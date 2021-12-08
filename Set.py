#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 08:17:07 2021

@author: hassan
"""

class Set:
    def __init__(self):
        self._theElements = list()
    def add(self,item):
        if item not in self._theElements:
            self._theElements.append(item)
    def remove(self,item):
        assert self.__contains__(item),"Item not in the Set"
        self._theElements.remove(item)
    def __len__(self):
        return len(self._theElements)
    def __contains__(self,item):
        return item in self.theElements
    def isSubsetOf( self,setB):
        for element in self:
            if element not in setB:
                return False
        return True
    def union( self, setB ):
        newSet = Set()
        newSet._theElements.extend( self._theElements )
        for element in setB :
            if element not in self :
                newSet._theElements.append( element )
        return newSet
    def interset( self, setB ):
        newSet = Set()
        for element in setB :
            if element in self :
                newSet._theElements.append( element )
        return newSet
    def difference( self, setB ):
        newSet = Set()
        for element in self :
            if element not in setB :
                newSet._theElements.append( element )
        return newSet
    def __eq__( self, setB ):
        if len( self ) != len( setB ) :
            return False
        else :
            return self.isSubsetOf( setB )
    def __iter__( self ):
        return _SetIterator( self._theElements )
class _SetIterator :
    def __init__( self, setElements ):
        self._setRef = setElements
        self._curNdx = 0
    def __iter__( self ):
        return self
    def __next__( self ):
        if self._curNdx < len( self._setRef ) :
            entry = self._setRef[ self._curNdx ]
            self._curNdx += 1
            return entry
        else :
            raise StopIteration
