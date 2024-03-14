class Graph:
    def __init__(self, vertices):
        self.graph_dict = {}
        self.num_vertices = vertices

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 not in self.graph_dict:
            self.graph_dict[vertex1] = {}
        self.graph_dict[vertex1][vertex2] = weight

        if vertex2 not in self.graph_dict:
            self.graph_dict[vertex2] = {}
        self.graph_dict[vertex2][vertex1] = weight

    def dijkstra(self, start_vertex):
        distances = {}
        path = [float('inf')] * self.num_vertices
        path[start_vertex - 1] = 0
        current_vertex = start_vertex

        for vertex in self.graph_dict:
            distances[vertex] = float('inf')

        while distances:
            current_distance = path[current_vertex - 1]
            for neighbor_vertex in self.graph_dict[current_vertex]:
                if neighbor_vertex in distances:
                    distances[neighbor_vertex] = min(distances[neighbor_vertex], current_distance + self.graph_dict[current_vertex][neighbor_vertex])
                    path[neighbor_vertex - 1] = distances[neighbor_vertex]
            del distances[current_vertex]
            if distances:
                current_vertex = min(distances, key=distances.get)

        for vertex in self.graph_dict:
            print(f"Minimum Distance of vertice {vertex} from {start_vertex} is {path[vertex - 1]}")


g = Graph(9)
g.add_edge(1, 2, 4)
g.add_edge(1, 8, 8)
g.add_edge(2, 3, 8)
g.add_edge(2, 8, 11)
g.add_edge(3, 4, 7)
g.add_edge(3, 6, 4)
g.add_edge(3, 9, 2)
g.add_edge(4, 5, 9)
g.add_edge(4, 6, 14)
g.add_edge(5, 6, 10)
g.add_edge(6, 7, 2)
g.add_edge(7, 8, 1)
g.add_edge(7, 9, 6)
g.add_edge(8, 9, 7)

g.dijkstra(3)
