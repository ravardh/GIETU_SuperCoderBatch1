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
    for i in self.graph:
      print(f"{i}: {self.graph[i]}")
    
  def min_path(self, node): 
    '''
    min_path of all the others vertices from the start node
    '''
    # initially assume the minimum distance is infinity
    path = [float('inf')] * (self.V + 1)  
    path[node] = 0
    for i in self.graph:
      neighbour = self.graph[i]
      # if direct edge is present between start and ith node it's the smallest
      if node in neighbour:
        path[i] = neighbour[node]
      # update the neighbours of ith node with the minimum distance of neighbour and start node through ith node
      for j in neighbour:
        path[j] = min(path[j], path[i]+neighbour[j])
      
    # print the distance
    for i in self.graph:
      print(f"Minimum Distance of vertice {i} from {node} is {path[i]}")
    

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
g.min_path(1)