#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 17:20:28 2021

@author: hassan
"""
class _ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__( self ):
        return self._size   
    def contain(self,data):
        curr = self._head
        while curr.next is not self._head and curr.data != data:
            curr = curr.next
        if curr.data != data:
            return False
        return curr is not None
    def add_to_begin(self,data):
        newNode = _ListNode(data)
          #Add the first element in the linked list
        if self._size == 0:
            self._head = newNode
            self._head.next = self._head
            self._tail = self._head
            self._size += 1
            return
        newNode.next = self._head
        self._tail.next = newNode
        self._head = newNode
        self._size += 1
    def add_to_end(self,data):
        newNode = _ListNode(data)
          #Add the first element in the linked list
        if self._size == 0:
            self._head = newNode
            self._head.next = self._head
            self._tail = self._head
            self._size += 1
            return
        newNode.next = self._head
        self._tail.next = newNode
        self._tail = newNode
        self._size += 1
    def add_to_index(self,data,index):
        assert self._size > 0,"List doesn't contain any elements"
        assert self.contain(index) ,"Index Not Found"
        newNode = _ListNode(data)
        if index == self._head.data:
            self.add_to_begin(data)
            return
        curr = self._head
        pre = None
        while curr.next != None and curr.data != index:
            pre = curr
            curr = curr.next
        newNode.next = curr
        pre.next = newNode
        self._size += 1
    
    def remove(self,data):
        assert self._size > 0,"List doesn't contain any elements"
        
        
        if self._head.data == data:
            self._tail.next = self._head.next
            self._head = self._head.next
            self._size -= 1
            return
        assert self.contain(data) ,"Element Not Found"
        curr = self._head.next
        pre = self._head
        while curr is not self._head and curr.data != data:
            pre = curr
            curr = curr.next
            
        if self._tail.data == curr.data:
            pre.next = self._head
            self._tail = pre
            self._size -= 1
            return   
        
        pre.next = curr.next
        self._size -= 1
        return
        
            
    def traversal(self):
        assert self._size > 0,"List doesn't contain any elements"
        curr = self._head
        while curr.next is not self._head :
            print (curr.data)
            curr = curr.next
        print (curr.data)
    def __iter__( self ):
        return _CircularLinkedListIterator( self._head )
class _CircularLinkedListIterator :
    def __init__( self, listHead ):
        self._curNode = listHead
        self.Head = listHead
    def __iter__( self ):
        return self
    def next( self ):
        if self._curNode.next is self.Head :
            raise StopIteration
        else :
            item = self._curNode.data
            self._curNode = self._curNode.next
            return item 
a = CircularLinkedList()
a.add_to_end(7)
a.add_to_end(8)
a.add_to_begin(4)
a.add_to_end(100)
a.add_to_begin(0)
a.add_to_begin(3)
print(a.contain(7))
a.traversal()
print('-----------------------------')
a.add_to_index(5,3)
a.add_to_index(111,100)
a.remove(0)
a.traversal()