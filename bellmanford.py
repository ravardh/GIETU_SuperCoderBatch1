class Graph:
    def __init__(self,v):
        self.v = v
        self.adj_list = [[] for _ in range(v)]
        self.list=[float('inf') for _ in range(v)]
        self.dict={}
        for i in range(1,v+1):
            self.dict[i]=float('inf')
        
    def add_edge(self,s,d,w):
        self.adj_list[s-1].append((s,d,w))
        
    def dijkstra(self,s):
        self.dict[s]=0
        while len(self.dict)!=0:
            value=min(self.dict.values())
            keys=[i for i in self.dict if self.dict[i]==value]
            key=keys[0]
            self.dict.pop(key)
            self.list[key-1]=value
            for i in range(len(self.adj_list[key-1])):
                x=self.adj_list[key-1][i][1]
                d=self.adj_list[key-1][i][2]
                if x in self.dict.keys():
                    if self.dict[x]>value+d:
                        self.dict[x]=value+d
            
        print(self.list)

graph = Graph(9)
graph.add_edge(1,2,4)
graph.add_edge(1,8,8)
graph.add_edge(2,3,8)
graph.add_edge(2,8,11)
graph.add_edge(2,1,4)
graph.add_edge(3,2,8)
graph.add_edge(3,4,7)
graph.add_edge(3,9,2)
graph.add_edge(3,6,4)
graph.add_edge(4,3,7)
graph.add_edge(4,5,9)
graph.add_edge(4,6,14)
graph.add_edge(5,4,9)
graph.add_edge(5,6,10)
graph.add_edge(6,4,14)
graph.add_edge(6,5,10)
graph.add_edge(6,3,4)
graph.add_edge(6,7,2)
graph.add_edge(7,6,2)
graph.add_edge(7,9,6)
graph.add_edge(7,8,1)
graph.add_edge(8,9,7)
graph.add_edge(8,7,1)
graph.add_edge(8,2,11)
graph.add_edge(8,1,8)
graph.add_edge(9,3,2)
graph.add_edge(9,7,6)
graph.add_edge(9,8,7)

graph.dijkstra(3)