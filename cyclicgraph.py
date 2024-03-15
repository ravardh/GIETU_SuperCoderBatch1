from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

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
        for node in range(self.V):
            if not visited[node]:
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True
        return False

if __name__ == "__main__":
    graph = Graph(11)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 10)
    graph.add_edge(2, 1)
    graph.add_edge(2, 4)
    graph.add_edge(3, 1)
    graph.add_edge(3, 7)
    graph.add_edge(4, 2)
    graph.add_edge(4, 5)
    graph.add_edge(4, 7)
    graph.add_edge(4, 8)
    graph.add_edge(5, 4)
    graph.add_edge(5, 6)
    graph.add_edge(6, 5)
    graph.add_edge(6, 9)
    graph.add_edge(6, 10)
    graph.add_edge(7, 3)
    graph.add_edge(7, 4)
    graph.add_edge(7, 11)
    graph.add_edge(8, 4)
    graph.add_edge(8, 9)
    graph.add_edge(9, 6)
    graph.add_edge(9, 8)
    graph.add_edge(10, 1)
    graph.add_edge(10, 6)
    graph.add_edge(11, 7)

    if graph.is_cyclic():
        print("Graph contains cycle")
    else:
        print("Graph does not contain cycle")
