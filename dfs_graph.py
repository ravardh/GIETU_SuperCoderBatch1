'''class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.adj_list = [[] for _ in range(vertex)]
        self.visited = set()

    def add_edge(self, r, s):
        self.adj_list[r-1].append((r, s))

    def dfs(self, node):
        if node not in self.visited:
            print(node, end=" ")
            self.visited.add(node)
        for edge in self.adj_list[node-1]:
            x = edge[1]
            if x not in self.visited:
                self.dfs(x)

graph = Graph(11)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 10)
graph.add_edge(2, 4)
graph.add_edge(2, 1)
graph.add_edge(3, 1)
graph.add_edge(3, 7)
graph.add_edge(4, 5)
graph.add_edge(4, 2)
graph.add_edge(4, 7)
graph.add_edge(4, 8)
graph.add_edge(5, 4)
graph.add_edge(5, 6)
graph.add_edge(6, 10)
graph.add_edge(6, 9)
graph.add_edge(7, 11)
graph.add_edge(7, 3)
graph.add_edge(7, 4)
graph.add_edge(8, 4)
graph.add_edge(8, 9)
graph.add_edge(9, 6)
graph.add_edge(9, 8)
graph.add_edge(10, 6)
graph.add_edge(10, 1)
graph.add_edge(11, 7)

graph.dfs(1)'''

class Graph:
    def __init__(self, v):
        self.v = v
        self.adj_list = [[] for _ in range(v)]

    def add_edge(self, s, d):
        self.adj_list[s-1].append(d-1)

    def dfs(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')

        for neighbor in self.adj_list[vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def dfs_traversal(self, start):
        visited = set()
        self.dfs(start-1, visited)

    def display_graph(self):
        print(self.adj_list)
        for vertex in range(self.v):
            neighbors = self.adj_list[vertex]
            print(f"Vertex {vertex+1}: {neighbors}")


graph = Graph(11)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 10)
graph.add_edge(2, 4)
graph.add_edge(2, 1)
graph.add_edge(3, 1)
graph.add_edge(3, 7)
graph.add_edge(4, 5)
graph.add_edge(4, 2)
graph.add_edge(4, 7)
graph.add_edge(4, 8)
graph.add_edge(5, 4)
graph.add_edge(5, 6)
graph.add_edge(6, 10)
graph.add_edge(6, 9)
graph.add_edge(7, 11)
graph.add_edge(7, 3)
graph.add_edge(7, 4)
graph.add_edge(8, 4)
graph.add_edge(8, 9)
graph.add_edge(9, 6)
graph.add_edge(9, 8)
graph.add_edge(10, 6)
graph.add_edge(10, 1)
graph.add_edge(11, 7)

print("DFS traversal starting from vertex 1:")
graph.dfs_traversal(1)