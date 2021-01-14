#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 15:17:43 2021

@author: hassan
"""
class StackList:
    def __init__(self):
        self._stack = list()
    def push(self, item):
        self._stack.append(item)
    def pop(self):
        assert not self.isEmpty(), "Stack Is Empty"
        return self._stack.pop()
    def  peek(self):
        assert not self.isEmpty(), "Stack Is Empty"
        print(self._stack[-1])
    def __len__(self):
        return len(self._stack)
    def isEmpty(self):
        return self.__len__() == 0
    
class Stack:
    def __init__(self):
        self._size = 0
        self._top = -1
    def isEmpty( self ):
        return self._top == -1
    def __len__( self ):
        return self._size
    def push(self,item):
        self._top = _StackNode(item,self._top)
        self._size += 1
    def pop(self):
        assert not self.isEmpty(), "Stack Is Empty"
        node = self._top
        self._top = self._top.next
        self._size -= 1
        return node.item
    def  peek(self):
        assert not self.isEmpty(), "Stack Is Empty"
        print(self._top.item)
class _StackNode:
    def __init__(self,item,link):
        self.item = item
        self.next = link
    
    
    
a = StackList()
a.push(5)
a.push(10)
a.peek()
a.pop()
print(a.isEmpty())
b = Stack()
b.push(8)
b.push(16)
b.peek()
b.pop()
print(b.isEmpty())
