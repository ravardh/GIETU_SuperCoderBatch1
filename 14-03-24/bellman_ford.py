class Graph:
    def __init__(self,v):
        self.v = v
        self.adj_list = [[] for _ in range(v)]
        self.dict={}
        for i in range(1,v+1):
            self.dict[i]=float('inf')
        
    def add_edge(self,s,d,w):
        self.adj_list[s-1].append((s,d,w))
        
    def bellman_ford(self,source):
        self.dict[source]=0
        for i in range(self.v-1):
            for s,d,w in self.adj_list[i]:
                if self.dict[s]!=float('inf') and self.dict[d]>self.dict[s]+w:
                    self.dict[d]=self.dict[s] + w
        print(self.dict)
               
graph = Graph(7)
graph.add_edge(1,2,6)
graph.add_edge(1,3,5)
graph.add_edge(1,4,5)
graph.add_edge(2,5,-1)
graph.add_edge(3,2,-2)
graph.add_edge(3,5,1)
graph.add_edge(4,3,-2)
graph.add_edge(4,6,-1)
graph.add_edge(5,7,3)
graph.add_edge(6,7,3)
graph.bellman_ford(1)