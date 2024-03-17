class Graph:
  def __init__(self, vertices):
    self.graph = {}
    self.V = vertices

  def add_edge(self, u, v, w):
    if u not in self.graph:
      self.graph[u] = {}
    self.graph[u][v] = w

    if v not in self.graph:
      self.graph[v] = {}
    self.graph[v][u] = w

  def print_graph(self):
    print("{")
    for i in self.graph:
      print(f"  {i}: {self.graph[i]}")
    print("}")
    
  def dijsktra(self, start):  
    d = {}
    
    path = {}
    for i in self.graph:
      path[i] = float('inf')
    path[start] = 0
    k = start

    for i in self.graph:
      d[i] = float('inf')

    while len(d.keys()):
      v = path[k]
      for i in self.graph[k]:
        if i in d:
          d[i] = min(d[i], v+self.graph[k][i])
          path[i] = d[i]
      del d[k]
      if len(d):
        k = min(d, key=d.get)

    
    for i in self.graph:
      print(f"Minimum Distance of vertice {i} from {start} is {path[i]}")

g = Graph(9)
g.add_edge(1, 2, 4)
g.add_edge(1, 8, 8)
g.add_edge(2, 3, 8)
g.add_edge(2, 8, 11)
g.add_edge(3, 4, 7)
g.add_edge(3, 6, 4)
g.add_edge(3, 9, 2)
g.add_edge(4, 5, 9)
g.add_edge(4, 6, 14)
g.add_edge(5, 6, 10)
g.add_edge(6, 7, 2)
g.add_edge(7, 8, 1)
g.add_edge(7, 9, 6)
g.add_edge(8, 9, 7)

g.print_graph()
print()
g.dijsktra(3)
