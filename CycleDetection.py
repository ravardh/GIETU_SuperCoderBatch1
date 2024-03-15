class Graph:
    def __init__(self, v):
        self.v = v
        self.adj_list = [[] for _ in range(v)]

    def add_edge(self, s, d):
        self.adj_list[s - 1].append(d)
        self.adj_list[d - 1].append(s)  # Add reverse edge for undirected graph

    def dfs(self, vertex, parent, visited):
        visited.add(vertex)

        for neighbor in self.adj_list[vertex - 1]:
            if neighbor == parent:
                continue  # Skip visiting the parent
            if neighbor in visited or self.dfs(neighbor, vertex, visited):
                return True  # Cycle detected

        return False

    def is_cyclic(self):
        visited = set()

        for vertex in range(1, self.v + 1):
            if vertex not in visited:
                if self.dfs(vertex, None, visited):
                    return True  # Cycle detected

        return False  # No cycle detected

graph = Graph(7)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(3, 5)
graph.add_edge(5, 6)
graph.add_edge(6, 7)

print("Is graph cyclic?", graph.is_cyclic())