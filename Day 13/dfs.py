class Graph:
  def __init__(self):
    self.graph = {}

  def add_edge(self, u, v):
    if u not in self.graph:
      self.graph[u] = []
    self.graph[u].append(v)

  def print_adjacency_list(self):
    for i in self.graph:
      print(f"{i}: {self.graph[i]}")

  def dfs(self, start_vertex, visited=None):
    if visited is None:
      visited = set()

    if start_vertex not in visited:
      visited.add(start_vertex)
      print(start_vertex, end=" ")
      for child in self.graph[start_vertex]:
        self.dfs(child, visited)

g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 10)
g.add_edge(2, 1)
g.add_edge(2, 4)
g.add_edge(3, 1)
g.add_edge(3, 7)
g.add_edge(4, 2)
g.add_edge(4, 5)
g.add_edge(4, 7)
g.add_edge(4, 8)
g.add_edge(5, 4)
g.add_edge(5, 6)
g.add_edge(6, 5)
g.add_edge(6, 9)
g.add_edge(6, 10)
g.add_edge(7, 3)
g.add_edge(7, 4)
g.add_edge(7, 11)
g.add_edge(8, 4)
g.add_edge(8, 9)
g.add_edge(9, 6)
g.add_edge(9, 8)
g.add_edge(10, 1)
g.add_edge(10, 6)
g.add_edge(11, 7)

g.print_adjacency_list()

g.dfs(list(g.graph.keys())[0])
