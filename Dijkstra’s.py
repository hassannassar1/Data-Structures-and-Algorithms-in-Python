#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 18:15:56 2021

@author: hassan
"""
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

infinity = float('inf')

def find_lowest_cost_node(costs,processed):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def dijkstra(graph,start,end):
    
    costs = {}
    parents = {}
    processed = []
    
    for k in graph[start].keys():
        costs[k] = graph[start][k]
        parents[k]=start
    costs['fin'] = infinity
    parents['fin'] = None
    
    node = find_lowest_cost_node(costs,processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs,processed)
        
    return parents,costs

print(dijkstra(graph,'start','fin'))