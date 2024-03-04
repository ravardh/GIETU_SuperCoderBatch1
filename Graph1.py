# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 10:52:06 2024

@author: HP
"""

def create(graph, src, dst, wt=1):
    graph[src-1].append((src, dst, wt))
    
v = 9
graph = [[ ] for _ in range (v)]
for i in range(v):
    graph[i] = []
   
    
create(graph,1,2)
for g in graph:
    print(g)
create(graph,1,3)
for g in graph:
    print(g)
create(graph,1,9)
for g in graph:
    print(g)
create(graph,2,4)
for g in graph:
    print(g)
create(graph,2,1)
for g in graph:
    print(g)
create(graph,3,1)
for g in graph:
    print(g)
create(graph,3,4)
for g in graph:
    print(g)
create(graph,3,5)
for g in graph:
    print(g)
create(graph,3,7)
for g in graph:
    print(g)
create(graph,4,6)
for g in graph:
    print(g)
create(graph,4,2)
for g in graph:
    print(g)
create(graph,5,3)
for g in graph:
    print(g)

    