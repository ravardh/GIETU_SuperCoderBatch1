class Graph:
  def __init__(self, vertices):
    self.graph = {}
    self.V = vertices

  def add_edge(self, u, v, w):
    if u not in self.graph:
      self.graph[u] = {}
    self.graph[u][v] = w

  def print_graph(self):
    print("{")
    for i in self.graph:
      print(f"  {i}: {self.graph[i]}")
    print("}")
  

  ''' Algorithm for Bellman Ford [deals with -ve weight too]
      Create the edge list
      Initialize all vertex to infinity except source which is set to zero
      
      keep updating the minimum path of each vertex (V-1) times since it is proven after V times it will reach an optimum point
        curr = path[source] # minimum value upto source until now
        path[destination] = min(path[destination], curr+weight(source, destination))
  '''
  def bellman_ford(self, start):  # Sir's approach
    edge_list = []
    for i in self.graph:
      for j in self.graph[i]:
        edge_list.append((i, j))
    print(edge_list)
    
    path = {}
    for i in self.graph:
      path[i] = float('inf')
    print(path)
    path[start] = 0
    
    for i in range(self.V - 1):
      for j in edge_list:
        s = path[j[0]]
        path[j[1]] = min(path[j[1]], s+self.graph[j[0]][j[1]])


    # print the distance
    for i in self.graph:
      print(f"Minimum Distance of vertice {i} from {start} is {path[i]}")

g = Graph(7)
g.add_edge(1, 2, 6)
g.add_edge(1, 3, 5)
g.add_edge(1, 4, 5)
g.add_edge(2, 5, -1)
g.add_edge(3, 2, -2)
g.add_edge(3, 5, 1)
g.add_edge(4, 3, -2)
g.add_edge(4, 6, -1)
g.add_edge(5, 7, 3)
g.add_edge(6, 7, 3)
g.add_edge(7, 7, 0)

g.print_graph()
print()
# g.min_path(1)
g.bellman_ford(1)