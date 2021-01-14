#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 17:06:21 2021

@author: hassan
"""

class Bag:
    def __init__(self):
        self._theItems = list()
    
    def __len__(self):
        return len(self._theItems)
    def add(self,item):
        self._theItems.append(item)
    def remove(self,item):
        assert item in self._theItems,"Item isn't in the bag"
        self._theItems.remove(item)
    def __contain__(self,item):
        if item in self._theItems:
            return True
        return False
    def __iter__( self ):
        return _BagIterator( self._theItems )
    
class _BagIterator :
    def __init__( self, theList ):
        self._bagItems = theList
        self._curItem = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._curItem < len(self._bagItems):
            item = self._bagItems[self._curItem]
            self._curItem += 1
            return item
        else :
            raise StopIteration
            
bag = Bag()
bag.add(5)
bag.add(6)
bag.add(7)
bag.__contain__(6)
bag.remove(6)  
bag.__contain__(6)
bag.__len__()
for item in bag:
    print(item)