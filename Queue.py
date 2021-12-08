#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 15:54:17 2021

@author: hassan
"""

class QueueList:
    def __init__(self):
        self._queue = list()
    def enqueue(self, item):
        self._queue.append(item)
    def dequeue(self):
        assert not self.isEmpty(), "Queue Is Empty"
        return self._queue.pop(0)
    def __len__(self):
        return len(self._queue)
    def isEmpty(self):
        return self.__len__() == 0
    
class Queue:
    def __init__(self):
        self._count = 0
        self._front = None
        self._back = None
    def isEmpty( self ):
        return self._front is None
    def __len__( self ):
        return self._count
    
    def enqueue( self, item ):
        node = _QueueNode( item )
        if self.isEmpty() :
            self._front = node
        else :
            self._back.next = node
        self._back = node
        self._count += 1
        
    def dequeue( self ):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        node = self._front
        if self._front is self._back :
            self._back = None
        self._front = self._front.next
        self._count -= 1
        return node.item
            
class _QueueNode( object ):
    def __init__( self, item ):
        self.item = item
        self.next = None
    
Q = Queue()
Q.enqueue( 28 )
Q.enqueue( 19 )
Q.enqueue( 45 )
Q.enqueue( 13 )
Q.enqueue( 7 ) 
print(Q.dequeue())