#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 15:35:27 2021

@author: hassan
"""

class ListNode :
    def __init__( self, data ) :
        self.data = data
        self.next = None
class LinkedList:
    
    def __init__(self,data):
        self._head = ListNode(data)
        self.size = 0
        
    def __len__( self ):
        return self._size   
    def contain(self,data):
        curr = self._head
        while curr.next is not None and curr.data != data:
            curr = curr.next
        if curr.data != data:
            return False
        return curr is not None
    
    def add_to_begin(self,data):
        newNode = ListNode(data)
        newNode.next = self._head
        self._head = newNode
        self.size += 1
        
    def add_to_end(self,data):
        newNode = ListNode(data)
        curr = self._head
        while curr.next != None:
            curr = curr.next
        curr.next = newNode
        self.size += 1
    def add_to_index(self,data,index):
        assert self.size > 0,"List doesn't contain any elements"
        assert self.contain(index) ,"Index Not Found"
        newNode = ListNode(data)
        curr = self._head
        pre = None
        while curr.next != None and curr.data != index:
            pre = curr
            curr = curr.next
        if curr is self._head:
            newNode.next =  self._head
            self._head = newNode
            return
        newNode.next = curr
        pre.next = newNode
        self.size += 1
    def remove(self,data):
        assert self.size > 0,"List doesn't contain any elements"
        if self._head.data==data:
            self._head = self._head.next
            self.size -= 1
            return
            
        curr = self._head.next
        pre = self._head
        while curr.next:
            if curr.data==data:
                pre.next = curr.next
                self.size -= 1
                return
            pre = curr
            curr = curr.next
            if curr.data==data and curr.next==None:
                pre.next = None
                self.size -= 1
                return
                
        return 
            
    def traversal(self):
        assert self.size > 0,"List doesn't contain any elements"
        curr = self._head
        while curr is not None :
            print (curr.data)
            curr = curr.next
    def __iter__( self ):
        return _LinkedListIterator( self._head )
class _LinkedListIterator :
    def __init__( self, listHead ):
        self._curNode = listHead
    def __iter__( self ):
        return self
    def next( self ):
        if self._curNode is None :
            raise StopIteration
        else :
            item = self._curNode.item
            self._curNode = self._curNode.next
            return item    
a = LinkedList(5)
a.add_to_end(7)
a.add_to_end(8)
a.add_to_begin(4)
a.add_to_end(100)
a.add_to_begin(0)
a.traversal()
print(a.contain(112))
a.add_to_index(11,0)
print('-----------------')
a.traversal()



'''
    def unorderedSearch( self, target ):
        curNode = self.head
        while curNode is not None and curNode.data != target :
            curNode= curNode.next
        return curNode is not None
        '''