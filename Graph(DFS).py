class Graph:
    def __init__(self,v):
        self.v = v
        self.adj_list = [[] for _ in range(v)]
        self.visited = [] 

    def add_edge(self,s,d,w):
        self.adj_list[s-1].append((s,d,w))

    # def dfs(self,start):
    #     visited = set()
    #     queue = [start]
    def dfs(self, start):
        
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


graph = Graph(11)
graph.add_edge(1,10,1)
graph.add_edge(1,2,1)
graph.add_edge(1,3,1)
graph.add_edge(2,4,1)
graph.add_edge(2,1,1)
graph.add_edge(3,1,1)
graph.add_edge(3,7,1)
graph.add_edge(4,2,1)
graph.add_edge(4,5,1)
graph.add_edge(4,7,1)
graph.add_edge(4,8,1)
graph.add_edge(5,4,1)
graph.add_edge(5,6,1)
graph.add_edge(6,5,1)
graph.add_edge(6,9,1)
graph.add_edge(6,10,1)
graph.add_edge(7,11,1)
graph.add_edge(7,3,1)
graph.add_edge(7,4,1)
graph.add_edge(8,9,1)
graph.add_edge(8,4,1)
graph.add_edge(9,6,1)
graph.add_edge(9,8,1)
graph.add_edge(10,1,1)
graph.add_edge(10,6,1)
graph.bfs(4)
