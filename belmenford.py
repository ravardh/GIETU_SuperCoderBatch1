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
        print("Vertex   Distance from Source")
        for i in range(self.V):
            print(f"{i} \t\t {distance[i]}")

edges = [(1, 2, 6), (1, 3, 5), (1, 4, 5), (2, 5, 1), (3, 2, -2), (3, 5, 1), (4, 3, -2), (4, 6, -1), (5, 7, 3), (6, 7, 3)]
num_vertices = 7  

graph = Graph(num_vertices)
for edge in edges:
    graph.add_edge(edge[0], edge[1], edge[2])

source_vertex = 0  
graph.bellman_ford(source_vertex)
