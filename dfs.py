class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        neighbors = self.graph.get(v, [])
        for neighbor in neighbors:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = {}
        self.dfs_util(start, visited)

g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 9)
g.add_edge(2, 1)
g.add_edge(2, 4)
g.add_edge(3, 1)
g.add_edge(3, 8)
g.add_edge(4, 2)
g.add_edge(4, 5)
g.add_edge(4, 6)
g.add_edge(5, 4)
g.add_edge(6, 4)
g.add_edge(6, 7)
g.add_edge(7, 6)
g.add_edge(7, 8)
g.add_edge(8, 7)
g.add_edge(8, 9)
g.add_edge(8, 3)
g.add_edge(9, 8)
g.add_edge(9, 1)

print("DFS Traversal:")
g.dfs(2)
