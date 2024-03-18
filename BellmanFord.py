class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, src):
        # Initialize distances from src to all other vertices as infinite
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Relax all edges |V| - 1 times
        for _ in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of the picked vertex
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Check for negative-weight cycles
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        # Print the calculated distances
        self.print_solution(dist)

    def print_solution(self, dist):
        print("Vertex \t Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")


# Example usage:
g = Graph(5)

g.add_edge(1, 2, 6)
g.add_edge(1, 3, 5)
g.add_edge(1, 4, 5)
g.add_edge(2, 5, -1)
g.add_edge(3, 2, -2)
g.add_edge(3, 5, 1)
g.add_edge(5,7 , 3)
g.add_edge(4, 3, -2)
g.add_edge(4, 6, -1)

# Run Bellman-Ford algorithm from vertex 0
g.bellman_ford(0)