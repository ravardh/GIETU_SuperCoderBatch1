class Graph:
    def __init__(self,v):
        self.v = v
        self.adj_list = [[] for _ in range(v)]
        self.visited=set()

    def edge(self,s,d,w):
        self.adj_list[s-1].append((s,d,w))
        
    def DFS(self,v):
        
        self.visited.add(v)
        for i in range(len(self.adj_list[v-1])):
            x=self.adj_list[v-1][i][1]
            if x not in self.visited:
                self.DFS(x)
        print(v, end=' ')
                
                
graph = Graph(11)
graph.edge(1,3,1)
graph.edge(1,2,1)
graph.edge(1,10,1)
graph.edge(2,1,1)
graph.edge(2,4,1)
graph.edge(3,1,1)
graph.edge(3,7,1)
graph.edge(4,5,1)
graph.edge(4,2,1)
graph.edge(4,7,1)
graph.edge(4,8,1)
graph.edge(5,4,1)
graph.edge(5,6,1)
graph.edge(6,10,1)
graph.edge(6,9,1)
graph.edge(7,4,1)
graph.edge(7,3,1)
graph.edge(7,11,1)
graph.edge(8,4,1)
graph.edge(8,9,1)
graph.edge(9,6,1)
graph.edge(9,8,1)
graph.edge(10,6,1)
graph.edge(10,1,1)
graph.edge(11,7,1)



graph.DFS(4)