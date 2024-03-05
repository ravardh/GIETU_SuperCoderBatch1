#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)

    def dfs_util(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=' ')

        for neighbor in self.adj_list[vertex]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = {vertex: False for vertex in self.adj_list}
        self.dfs_util(start, visited)


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    print("Depth First Traversal (starting from vertex 2):")
    graph.dfs(2)


# In[6]:


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for i in self.adj_list[v]:
            if not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start):
        visited = [False] * self.vertices
        self.dfs_util(start, visited)


graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

print("Adjacency List:")
for vertex, neighbors in enumerate(graph.adj_list):
    print(f"{vertex} -> {neighbors}")

print("\nDFS Traversal:")
graph.dfs(2)


# In[ ]:




