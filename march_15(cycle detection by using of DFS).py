#cycle detection by using of DFS
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
                    if self.dfs(neighbor, visited, traversal):
                        return True
                elif neighbor in traversal:
                    return True

        traversal.pop()
        return False

g = Graph()

g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 1)
g.add_edge(2, 4)
g.add_edge(3, 1)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 2)
g.add_edge(4, 3)
g.add_edge(5, 3)
g.add_edge(5, 6)
g.add_edge(6, 5)
g.add_edge(6, 7)
g.add_edge(7, 6)

cycle_detected = False
for node in g.graph:
    if g.dfs(node):
        cycle_detected = True
        break

if cycle_detected:
    print("Cycle detected")
else:
    print("No cycle detected")
Cycle detected.