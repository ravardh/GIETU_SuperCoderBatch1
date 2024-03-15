class Graph:
  def __init__(self, vertices):
    self.vertices = vertices
    self.adj_list = [[] for _ in range(vertices)]
    self.dict = {i: float('inf') for i in range(1, vertices + 1)}  # Include vertices 1 to n

  def add_edge(self, s, d, w):
    self.adj_list[s - 1].append((s, d, w))

  def shortest(self, s):
    self.dict[s] = 0
    vertex_map = {i: i + 1 for i in range(self.vertices)} 

    for _ in range(self.vertices):
      for i in range(len(self.adj_list)):
        for neighbor in self.adj_list[i]:
          x, d, w = neighbor
          if vertex_map[x] in self.dict.keys():  
            if self.dict[vertex_map[x]] > self.dict[i] + w:
                self.dict[vertex_map[x]] = self.dict[i] + w

graph = Graph(1 )
graph.add_edge(1, 2, 6)
graph.add_edge(1, 3, 5)
graph.add_edge(1, 4, 5)
graph.add_edge(2, 5, -1)
graph.add_edge(3, 2, -2)
graph.add_edge(3, 5, 1)
graph.add_edge(4, 3, -2)
graph.add_edge(4, 6, -1)
graph.add_edge(5, 7, 3)
graph.add_edge(6, 7, 3)

graph.shortest(3)

# Print the shortest distances from vertex 3
print(graph.dict)
