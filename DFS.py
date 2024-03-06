class Graph:
    def __init__(self, num_vertices):
        self.graph = [[ ] for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        num_vertices = len(self.graph)
        visited = [False] * num_vertices
        queue = [start]

        while queue:
            vertex = queue.pop(0)

            if not visited[vertex]:
                print(vertex, end=" ")
                visited[vertex] = True

                queue.extend(neighbor for neighbor in self.graph[vertex] if not visited[neighbor])

g = Graph(10)
g.add_edge(1, 2)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(4, 6)
g.add_edge(6, 7)
g.add_edge(7, 8)
g.add_edge(8, 9)
g.add_edge(9, 1)
g.add_edge(1, 3)
g.add_edge(3, 8)

print("BFS Traversal starting from vertex 1:")
g.bfs(1)