# Python3 program for Bellman-Ford's single source shortest path algorithm.
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # utility function used to print the solution
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    # The main function that finds shortest distances from src to
    # all other vertices using Bellman-Ford algorithm. The function
    # also detects negative weight cycle
    def BellmanFord(self, src):
        # Step 1: Initialize distances from src to all other vertices as INFINITE
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times.
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: Check for negative-weight cycles
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        # Print all distances
        self.printArr(dist)


# Driver's code
if __name__ == '__main__':
    g = Graph(8)
    g.addEdge(1, 2, 6)
    g.addEdge(1, 3, 5)
    g.addEdge(1, 4, 5)
    g.addEdge(2, 5, -1)
    g.addEdge(3, 2, -2)
    g.addEdge(3, 5, 1)
    g.addEdge(4, 3, -2)
    g.addEdge(4, 6, -1)
    g.addEdge(5, 7, 3)
    g.addEdge(6, 7, 3)

    # Function call
    g.BellmanFord(1)

