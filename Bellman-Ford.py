class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, src):
        distance = [float("Inf")] * self.V
        distance[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if distance[u] != float("Inf") and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

        for u, v, w in self.graph:
            if distance[u] != float("Inf") and distance[u] + w < distance[v]:
                print("Graph contains negative weight cycle")
                return

        self.print_solution(distance)

    def print_solution(self, distance):
        print("Vertex Distance from Source:")
        for i in range(self.V):
            print(f"{i}\t\t{distance[i]}")


g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

g.bellman_ford(0)

