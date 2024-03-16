class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[v] = False
        return False

    def is_cyclic(self):
        visited = [False] * self.V
        rec_stack = [False] * self.V

        for i in range(self.V):
            if not visited[i]:
                if self.is_cyclic_util(i, visited, rec_stack):
                    return True

        return False

# Example usage:
g = Graph(8)
g.add_edge(1, 2)
g.add_edge(2, 4)
g.add_edge(1, 3)
g.add_edge(3, 5)
g.add_edge(3, 4)
g.add_edge(5, 6)
g.add_edge(6, 7)
if(g.is_cyclic()):
    print("Cycle detected")
else:
    print("Cycle not present")
