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
vertices = 10
g = Graph(vertices)
g.add_edge(1,3)
g.add_edge(3,8)
g.add_edge(1,9)
g.add_edge(1,2)
g.add_edge(2,4)
g.add_edge(4,5)
g.add_edge(4,6)
g.add_edge(6,7)
g.add_edge(7,8)
g.add_edge(8,9)

print("BFS traversal:")
g.bfs(1)
