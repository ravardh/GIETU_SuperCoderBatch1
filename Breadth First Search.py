#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.adj_list = [[] for _ in range(vertex)]
        self.visited = set()

    def add_edge(self, r, s, m):
        self.adj_list[r-1].append((r, s, m))

    def bfs(self, start):
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in self.visited:
                print(node, end=" ")
                self.visited.add(node)
                for edge in self.adj_list[node-1]:
                    x = edge[1]
                    if x not in self.visited:
                        queue.append(x)

graph = Graph(9)
graph.add_edge(1, 2, 1)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 9, 1)
graph.add_edge(2, 4, 1)
graph.add_edge(2, 1, 1)
graph.add_edge(3, 1, 1)
graph.add_edge(3, 8, 1)
graph.add_edge(4, 5, 1)
graph.add_edge(4, 6, 1)
graph.add_edge(4, 2, 1)
graph.add_edge(5, 4, 1)
graph.add_edge(6, 4, 1)
graph.add_edge(6, 7, 1)
graph.add_edge(7, 6, 1)
graph.add_edge(7, 8, 1)
graph.add_edge(8, 3, 1)
graph.add_edge(8, 9, 1)
graph.add_edge(9, 1, 1)
graph.add_edge(9, 8, 1)

graph.bfs(1)


# In[ ]:




