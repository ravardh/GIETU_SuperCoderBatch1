class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def bellman_ford(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                print("Graph contains negative cycle")
                return

        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i} \t\t {dist[i]}")


g = Graph(8)
g.add_edge(1, 2, 6)
g.add_edge(1, 3, 5)
g.add_edge(1, 4, 5)
g.add_edge(2, 5, -1)
g.add_edge(3, 2, -2)
g.add_edge(4, 3, -2)
g.add_edge(4, 6, -1)
g.add_edge(6, 7, 3)
g.add_edge(5, 7, 3)
g.add_edge(3, 5, 1)

start_vertex = 1
g.bellman_ford(start_vertex)
