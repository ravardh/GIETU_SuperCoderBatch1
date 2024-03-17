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
    print("{")
    for i in self.graph:
      print(f"  {i}: {self.graph[i]}")
    print("}")

  def bfs(self, start_vertex):
    visited = set()
    queue = [start_vertex]
    front = 0

    while front < len(queue):
      vertex = queue[front]
      front += 1
      if vertex not in visited:
        visited.add(vertex)
        print(vertex, end=" ")
        for neighbour in self.graph[vertex]:
          if neighbour not in visited:
            queue.append(neighbour)

  def dfs(self, start_vertex, visited=None):
    if visited is None:
      visited = set()

    if start_vertex not in visited:
      visited.add(start_vertex)
      print(start_vertex, end=" ")
      for neighbour in self.graph[start_vertex]:
        self.dfs(neighbour, visited)

g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 10)
g.add_edge(2, 4)
g.add_edge(3, 7)
g.add_edge(4, 5)
g.add_edge(4, 7)
g.add_edge(4, 8)
g.add_edge(5, 6)
g.add_edge(6, 9)
g.add_edge(6, 10)
g.add_edge(7, 11)
g.add_edge(9, 8)

g.print_adjacency_list()

print("BFS")
g.bfs(list(g.graph.keys())[0])
print()
print("DFS")
g.dfs(list(g.graph.keys())[0])
