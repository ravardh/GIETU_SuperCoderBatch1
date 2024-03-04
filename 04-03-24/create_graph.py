class Graph:
    def __init__(self,v):
        self.v= v
        self.adj_list = [[] for _ in range(v)]

    def add_edge(self,s,d,w):
        self.adj_list[s-1].append((d,w))

    def display_graph(self):
        for vertex in range(self.v):
            neighbors = self.adj_list[vertex]
            print(f"Vertex {vertex + 1}: {neighbors}")
            
graph = Graph(5)
graph.add_edge(1,1,2)
graph.add_edge(1,4,3)
graph.add_edge(2,2,3)
graph.add_edge(2,3,4)
graph.add_edge(2,4,4)
graph.add_edge(3,3,4)
graph.add_edge(4,4,4)
graph.display_graph()
