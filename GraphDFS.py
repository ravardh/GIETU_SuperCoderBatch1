class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {vertex: [] for vertex in range(1, vertices + 1)}

    def add_edge(self, u, v, weight):
        self.adj_list[u].append((v, weight))

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")

        for neighbor, _ in self.adj_list[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)


graph = Graph(11)
graph.add_edge(1, 10, 1)
graph.add_edge(1, 2, 1)
graph.add_edge(1, 3, 1)
graph.add_edge(2, 4, 1)
graph.add_edge(2, 1, 1)
graph.add_edge(3, 1, 1)
graph.add_edge(3, 7, 1)
graph.add_edge(4, 2, 1)
graph.add_edge(4, 5, 1)
graph.add_edge(4, 7, 1)
graph.add_edge(4, 8, 1)
graph.add_edge(5, 4, 1)
graph.add_edge(5, 6, 1)
graph.add_edge(6, 5, 1)
graph.add_edge(6, 9, 1)
graph.add_edge(6, 10, 1)
graph.add_edge(7, 11, 1)
graph.add_edge(7, 3, 1)
graph.add_edge(7, 4, 1)
graph.add_edge(8, 9, 1)
graph.add_edge(8, 4, 1)
graph.add_edge(9, 6, 1)
graph.add_edge(9, 8, 1)
graph.add_edge(10, 1, 1)
graph.add_edge(10, 6, 1)

print("DFS Traversal:")
graph.dfs(1)
