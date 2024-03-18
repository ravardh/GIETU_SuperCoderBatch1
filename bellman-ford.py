class Graph:
    def __init__(self,v=None):
        self.v=v
        self.adj_list=[[] for _ in range(v)]
        self.visited=set()
    def add_edge(self,s,d,w):
        self.adj_list[s-1].append((s,d,w))
    def belman(self,s):
        distance={i:float("inf") for i in range(1,self.v+1)}
        print(distance)
        distance[s]=0
        print(distance)
        for x in range(self.v-1):
            for vertex in range(1,self.v+1):
                for source,destination,weight in self.adj_list[vertex-1]:
                    if(distance[s]!=float('inf') and distance[s]+weight<distance[destination]):
                         distance[destination] = distance[source] + weight
        return distance


if __name__=="__main__":
    g=Graph(7)
    g.add_edge(1,2,6)
    g.add_edge(1,3,5)
    g.add_edge(1,4,5)
    g.add_edge(2,5,-1)
    g.add_edge(3,2,-2)
    g.add_edge(3,5,1)
    g.add_edge(4,3,-2)
    g.add_edge(4,6,-1)
    g.add_edge(5,7,3)
    g.add_edge(6,7,3)
    s=1
    print(g.belman(s))
  