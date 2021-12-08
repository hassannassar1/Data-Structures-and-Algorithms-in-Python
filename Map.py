#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 08:51:12 2021

@author: hassan
"""
class _MapEntry :
    def __init__( self, key, value ):
        self.key = key
        self.value = value
class Map:
    def __init__(self):
        self._entryList = list()
    def add(self,key,value):
        ndx = self._findPosition( key )
        if ndx is not None : 
            self._entryList[ndx].value = value
            return False
        else :
            entry = _MapEntry( key, value )
            self._entryList.append( entry )
            return True
    def remove(self,key):
        ndx = self._findPosition( key )
        assert ndx is not None, "Invalid map key."
        self._entryList.pop( ndx )
    def valueOf( self, key ):
        ndx = self._findPosition( key )
        assert ndx is not None, "Invalid map key."
        return self._entryList[ndx].value
    def __len__(self):
        return len(self._entryList)
    def __contains__(self,key):
        ndx = self._findPosition( key )
        return ndx is not None
    def _findPosition( self, key ):
        for i in range( len(self) ) :
            if self._entryList[i].key == key :
                return i
        return None
    
    def __iter__( self ):
        return _MapIterator( self._entryList )
class _MapIterator :
    def __init__( self, mapElements ):
        self._mapRef = mapElements
        self._curNdx = 0
    def __iter__( self ):
        return self
    def __next__( self ):
        if self._curNdx < len( self._mapRef ) :
            entry = self._mapRef[ self._curNdx ]
            self._curNdx += 1
            return entry
        else :
            raise StopIteration
    