class Graph:
    def _init_(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def min_distance(self, dist, spt_set):
        min_dist = float("inf")
        min_index = -1
        for v in range(self.V):
            if not spt_set[v] and dist[v] < min_dist:
                min_dist = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [float("inf")] * self.V
        dist[src] = 0
        spt_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True

            for v in range(self.V):
                if (
                    not spt_set[v]
                    and self.graph[u][v]
                    and dist[u] + self.graph[u][v] < dist[v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]

        return dist

# Example usage
g = Graph(9)
g.graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0],
]

source_vertex = 0
shortest_distances = g.dijkstra(source_vertex)

print("Vertex \t Distance from Source")
for node in range(g.V):
    print(f"{node} \t {shortest_distances[node]}")