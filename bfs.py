class Graph:
    def __init__(self, v):
        self.v = v
        self.adj_list = [[] for _ in range(v)]  # 2D LIST

    def add_edge(self, s, d):
        self.adj_list[s].append((s, d))
        self.adj_list[d].append((d, s))  # Add this line for undirected graph

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=' ')

            for _, neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def display_graph(self):
        print("[", end="")
        for vertex in range(self.v):
            neighbors = self.adj_list[vertex]
            print(neighbors, end="")
            if vertex != self.v - 1:
                print(",", end="")
        print("]")

graph = Graph(9)  # NO OF GRAPHS
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 8)
graph.add_edge(1, 3)
graph.add_edge(2, 7)
graph.add_edge(3, 4)
graph.add_edge(3, 5)
graph.add_edge(5, 6)
graph.add_edge(6, 7)
graph.add_edge(7, 8)
graph.display_graph()

print("BFS traversal starting from vertex 5:")
graph.bfs(5)
