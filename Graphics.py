class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def print_graph(self):
        for vertex in self.graph:
            print(vertex, "->", " -> ".join(map(str, self.graph[vertex])))

# Example usage
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 9)
g.add_edge(2, 1)
g.add_edge(2, 4)
g.add_edge(3, 1)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(3, 7)
g.add_edge(4, 2)
g.add_edge(4, 6)
g.add_edge(5, 3)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(6, 5)
g.add_edge(6, 7)
g.add_edge(8, 7)
g.add_edge(8, 9)
g.add_edge(9, 8)
g.add_edge(9, 1)

g.print_graph()
