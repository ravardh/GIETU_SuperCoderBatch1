class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def addedge(self, u, v):
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
g.addedge(0, 1)
g.addedge(0, 2)
g.addedge(1, 2)
g.addedge(2, 3)
g.addedge(3, 4)

print("BFS traversal from node 0:")
g.bfs(0)
