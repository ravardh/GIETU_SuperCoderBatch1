class Graph:
    def __init__(self,v):
        self.v = v
        self.adj_list = [[] for _ in range(v)]

    def add_edge(self,s,d,w):
        self.adj_list[s-1].append((s,d,w))
        
    def dfs1(self,v,visited):
        visited.add(v)
        for i in range(len(self.adj_list[v-1])):
            x=self.adj_list[v-1][i][1]
            if x not in visited:
                self.dfs1(x, visited)
        print(v, end=' ')
                
    def dfs(self, v):
        print(self.adj_list)
        visited = set()
        self.dfs1(v, visited)
                
graph = Graph(11)
graph.add_edge(1,3,0)
graph.add_edge(1,2,0)
graph.add_edge(1,10,0)
graph.add_edge(2,1,0)
graph.add_edge(2,4,0)
graph.add_edge(3,1,0)
graph.add_edge(3,7,0)
graph.add_edge(4,5,0)
graph.add_edge(4,2,0)
graph.add_edge(4,7,0)
graph.add_edge(4,8,0)
graph.add_edge(5,4,0)
graph.add_edge(5,6,0)
graph.add_edge(6,10,0)
graph.add_edge(6,9,0)
graph.add_edge(7,4,0)
graph.add_edge(7,3,0)
graph.add_edge(7,11,0)
graph.add_edge(8,4,0)
graph.add_edge(8,9,0)
graph.add_edge(9,6,0)
graph.add_edge(9,8,0)
graph.add_edge(10,6,0)
graph.add_edge(10,1,0)
graph.add_edge(11,7,0)

print(graph)

graph.dfs(4)