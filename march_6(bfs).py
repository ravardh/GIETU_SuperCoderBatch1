#bfs
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = [start]
        traversal = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                traversal.append(node)
                visited.add(node)
                if node in self.graph:
                    for neighbor in self.graph[node]:
                        if neighbor not in visited:
                            queue.append(neighbor)

        return traversal

g = Graph()
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,9)
g.add_edge(2,4)
g.add_edge(3,8)
g.add_edge(4,5)
g.add_edge(4,6)
g.add_edge(6,7)
g.add_edge(7,8)
g.add_edge(8,9)

print("BFS Traversal starting from node 1:", g.bfs(1))
