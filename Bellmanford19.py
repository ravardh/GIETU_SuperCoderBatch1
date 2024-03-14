class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def print_arr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def bellman_ford(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        self.print_arr(dist)


g = Graph(8)

g.add_edge(1, 2, 6)
g.add_edge(1, 3, 5)
g.add_edge(1, 4, 5)
g.add_edge(2, 5, -1)
g.add_edge(3, 2, -2)
g.add_edge(3, 5, 1)
g.add_edge(4, 3, -2)
g.add_edge(4, 6, -1)
g.add_edge(5, 7, 3)
g.add_edge(6, 7, 3)


g.bellman_ford(1)
