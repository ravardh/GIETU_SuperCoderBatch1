#dijkstra
class Graph:
    def __init__(self,v=None):
        self.v=v
        self.graph=[[] for _ in range(v)]
    def add_edge(self,u,v,W):
        self.graph[u-1].append([v,W])
        self.graph[v-1].append([u,W])
        
def dijkstra(s,graph):
    Dic={}
    for i in range(1,len(graph)+1):
        Dic[i]=float('inf')
    Dic[s]=0
    l=[[] for _ in range(len(graph))]
    
    while(len(Dic)>0):
        min=float('inf')
        k=0
        for i in Dic:
            if(min>Dic[i]):
                min=Dic[i]
                k=i
        for i in range(len(graph[k-1])):
            if(graph[k-1][i][0] in Dic):
                if(Dic[graph[k-1][i][0]]>graph[k-1][i][1]+min):
                    Dic[graph[k-1][i][0]]=graph[k-1][i][1]+min
        Dic.pop(k)
        l[k-1]=min

    print(l)
        
        
    
        
        
        
    
if __name__=="__main__":
    g=Graph(9)
    g.add_edge(1,2,4)
    g.add_edge(1,8,8)
    g.add_edge(2,3,8)
    g.add_edge(2,8,11)
    g.add_edge(3,4,7)
    g.add_edge(3,6,4)
    g.add_edge(3,9,2)
    g.add_edge(4,5,9)
    g.add_edge(4,6,14)
    g.add_edge(5,6,10)
    g.add_edge(6,7,2)
    g.add_edge(7,9,6)
    g.add_edge(8,9,7)
    g.add_edge(8,7,1)
    s=3
    dijkstra(s,g.graph)
