class Graph:
    def __init__(self, v):
        self.v = v
        self.graPh = [[] for _ in range(v)]

    def add_edge(self, u, v):
        # Ensure both u and v are valid indices
        if 0 <= u < self.v and 0 <= v < self.v:
            self.graPh[u].append(v)
            self.graPh[v].append(u)
        else:
            print(f"Invalid edge: ({u}, {v})")

    def DFS(self, source, visited):
        for i in range(len(self.graPh[source])):
            if self.graPh[source][i] not in visited:
                visited.add(self.graPh[source][i])
                self.DFS(self.graPh[source][i], visited)
        print(source, end=" ")


graph = Graph(11)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 10)
graph.add_edge(2, 4)
graph.add_edge(3, 7)
graph.add_edge(7, 11)
graph.add_edge(4, 5)
graph.add_edge(4, 8)
graph.add_edge(5, 6)
graph.add_edge(8, 9)
graph.add_edge(6, 9)
graph.add_edge(6, 10)

source = 1
visited = set()
visited.add(source)

print("DFS traversal starting from vertex", source, ":")
graph.DFS(source, visited)
