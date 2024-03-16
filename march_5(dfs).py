#dfs
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start, visited=None, traversal=None):
        if visited is None:
            visited = set()
        if traversal is None:
            traversal = []

        visited.add(start)
        traversal.append(start)

        if start in self.graph:
            for neighbor in self.graph[start]:
                if neighbor not in visited:
                    self.dfs(neighbor, visited, traversal)

        return traversal

g = Graph()

g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,10)
g.add_edge(2,4)
g.add_edge(3,7)
g.add_edge(4,5)
g.add_edge(4,7)
g.add_edge(5,4)
g.add_edge(5,6)
g.add_edge(6,9)
g.add_edge(6,10)
g.add_edge(7,3)
g.add_edge(7,4)
g.add_edge(7,11)
g.add_edge(8,4)
g.add_edge(8,9)
g.add_edge(9,6)
g.add_edge(9,8)
g.add_edge(10,1)
g.add_edge(10,6)

print("DFS Traversal starting from node 4:", g.dfs(4))
