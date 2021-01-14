#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:30:17 2021

@author: hassan
"""
class PriorityQueue:
    def __init__(self):
        self._items = list()
    def isEmpty(self):
        return len(self._items) == 0
    def __len__(self):
        return len(self._items)
    def enqueue(self,item,priority):
        qitem = _PriorityQEntry(item, priority)
        self._items.append(qitem)
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        highest = self._items[0].priority
        c = 0
        for i in range( self.__len__() ) :
            if self._items[i].priority > highest :
                highest = self._items[i].priority
                c= i
        qitem = self._items.pop( c )
        return qitem.item

class _PriorityQEntry :
    def __init__( self, item, priority ):
        self.item = item
        self.priority = priority
        
Q = PriorityQueue(  )
Q.enqueue( "purple", 5 )
Q.enqueue( "black", 1 )
Q.enqueue( "orange", 3 )
Q.enqueue( "white", 0 )
Q.enqueue( "green", 1 )
Q.enqueue( "yellow", 5 )
while not Q.isEmpty() :
    item = Q.dequeue()
    print( item )