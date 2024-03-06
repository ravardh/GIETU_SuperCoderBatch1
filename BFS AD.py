class Graph:
    def __init__(self,v):
        self.v = v
        self.adj_list = [[] for _ in range(v)]
        

    def add_edge(self,s,d,w):
        self.adj_list[s-1].append((s,d,w))
        
    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                for i in range(len(self.adj_list[node-1])):
                    x=self.adj_list[node-1][i][1]
                    if x not in visited:
                        queue.append(x)
       
graph = Graph(9)
graph.add_edge(1,2,1)
graph.add_edge(1,3,1)
graph.add_edge(1,9,1)
graph.add_edge(2,4,1)
graph.add_edge(2,1,1)
graph.add_edge(3,1,1)
graph.add_edge(3,8,1)
graph.add_edge(4,5,1)
graph.add_edge(4,6,1)
graph.add_edge(4,2,1)
graph.add_edge(5,4,1)
graph.add_edge(6,4,1)
graph.add_edge(6,7,1)
graph.add_edge(7,6,1)
graph.add_edge(7,8,1)
graph.add_edge(8,3,1)
graph.add_edge(8,9,1)
graph.add_edge(9,1,1)
graph.add_edge(9,8,1)

graph.bfs(1)