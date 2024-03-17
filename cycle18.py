class Graph:
  def __init__(self):
    self.graph = {}

  def add_edge(self, u, v):
    if u not in self.graph:
      self.graph[u] = []
    self.graph[u].append(v)

    if v not in self.graph:
      self.graph[v] = []
    self.graph[v].append(u)

  def print_adjacency_list(self):
    for i in self.graph:
      print(f"{i}: {self.graph[i]}")

  def dfs(self, start, parent, visited=None):
    if visited is None:
      visited = set()

    if start not in visited:
      visited.add(start)
      for child in self.graph[start]:
        if child == parent:
          continue
        
        if child in visited:
          return True
      
      for child in self.graph[start]:
        if child not in visited:
          return self.dfs(child, start, visited)
    return False
      
g = Graph()
g.add_edge(1, 3)
g.add_edge(1, 2)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(6, 7)
g.add_edge(5, 6)

g.print_adjacency_list()


print(g.dfs(list(g.graph.keys())[0], -1))
