#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 16:50:28 2021

@author: hassan
"""
from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def bfs(graph,name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not(person in searched):
            print(person)
            if person[-1] == 'm':
                print(person + ' is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
                
    return False
bfs(graph,'you')