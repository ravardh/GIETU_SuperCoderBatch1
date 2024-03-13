class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u - 1].append(v - 1)
        self.graph[v - 1].append(u - 1)

    def dfs(self, start_node, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_node)
        print(start_node + 1, end=" ")  # Adjusting the indexing

        for neighbor in self.graph[start_node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

vertices = 11
g = Graph(vertices)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 10)
g.add_edge(2, 4)
g.add_edge(3, 7)
g.add_edge(7, 11)
g.add_edge(7, 4)
g.add_edge(4, 8)
g.add_edge(4, 5)
g.add_edge(8, 9)
g.add_edge(5, 6)
g.add_edge(9, 6)
g.add_edge(6, 10)

print("DFS traversal")
g.dfs(0)