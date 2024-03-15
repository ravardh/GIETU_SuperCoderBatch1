class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.adj_list = [[] for _ in range(vertex)]
        self.visited = set()

    def add_edge(self, s, d,w):
        self.adj_list[s-1].append((s, d,w))

    def dfs(self,v):
        
        if v not in self.visited:
            print(v, end=" ")
            self.visited.add(v)
        for edge in  range(len(self.adj_list[v-1])):
            x = edge[1]
            if x not in self.visited:
                self.dfs(x)
        print(v,end=' ')

       
        
        

graph = Graph(11)
graph.add_edge(1, 2,1)
graph.add_edge(1, 3,1)
graph.add_edge(1, 10,1)
graph.add_edge(2,4 ,1)
graph.add_edge(2, 1,1)
graph.add_edge(3, 1,1)
graph.add_edge(3, 7,1)
graph.add_edge(4, 5,1)
graph.add_edge(4, 2,1)
graph.add_edge(4, 7,1)
graph.add_edge(4, 8,1)
graph.add_edge(5, 4,1)
graph.add_edge(5, 6,1)
graph.add_edge(6, 10,1)
graph.add_edge(6, 9,1)
graph.add_edge(7, 11,1)
graph.add_edge(7, 3,1)
graph.add_edge(7, 4,1)
graph.add_edge(8, 4,1)
graph.add_edge(8, 9,1)
graph.add_edge(9, 6,1)
graph.add_edge(9, 8,1)
graph.add_edge(10, 6,1)
graph.add_edge(10, 1,1)
graph.add_edge(11, 7,1)

graph.dfs(11)





