#!/usr/bin/env python
# coding: utf-8

# In[1]:


import heapq

def prim(graph):
    num_vertices = len(graph)
    min_spanning_tree = []
    visited = [False] * num_vertices
    min_heap = []  
    start_vertex = '1'
    visited[int(start_vertex) - 1] = True
    total_weight = 0
    predecessor = {vertex: None for vertex in graph}

    for neighbor, neighbor_weight in graph[start_vertex]:
        heapq.heappush(min_heap, (neighbor_weight, start_vertex, neighbor))

    while min_heap:
        weight, src, dest = heapq.heappop(min_heap)
        if not visited[int(dest) - 1]:
            visited[int(dest) - 1] = True
            min_spanning_tree.append((weight, src, dest))
            total_weight += weight
            for neighbor, neighbor_weight in graph[dest]:
                if not visited[int(neighbor) - 1]:
                    heapq.heappush(min_heap, (neighbor_weight, dest, neighbor))
                    predecessor[neighbor] = dest

    return min_spanning_tree, total_weight

graph = {
    '1': [('2', 6), ('3', 5), ('5', 4)],
    '5': [('1', 4), ('4', 1), ('6', 8)],
    '6': [('5', 8), ('4', 7)],
    '4': [('3', 3), ('5', 1), ('8', 10), ('6', 7)],
    '8': [('4', 10), ('7', 9)],
    '7': [('3', 11), ('8', 9)],
    '3': [('1', 5), ('4', 3), ('7', 11), ('2', 2)],
    '2': [('1', 6), ('3', 2)],
}

min_spanning_tree, total_weight = prim(graph)
print("Minimum Spanning Tree:")
for weight, src, dest in min_spanning_tree:
    print(f"Edge: {src}-{dest} Weight: {weight}")
print(f"Total Weight: {total_weight}")


# In[ ]:




