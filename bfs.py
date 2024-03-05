class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start_node):
        visited = [False] * self.V
        queue = [start_node]
        visited[start_node] = True

        while queue:
            current_node = queue.pop(0)
            print(current_node, end=" ")

            for neighbor in self.graph[current_node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

# Example usage
vertices = 5
g = Graph(vertices)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)

print("BFS traversal starting from node 0:")
g.bfs(0)