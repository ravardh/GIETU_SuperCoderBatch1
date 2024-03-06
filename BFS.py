class Graph:
    adj = []
    def __init__(self, v, e):
         
        self.v = v
        self.e = e
        Graph.adj = [[0 for i in range(v)] 
                        for j in range(v)]
    def addEdge(self, start, e):
        Graph.adj[start][e] = 1
        Graph.adj[e][start] = 1
    def BFS(self, start):
        visited = [False] * self.v
        q = [start]

        visited[start] = True
 
        while q:
            vis = q[0]
            print(vis, end = ' ')
            q.pop(0)
            for i in range(self.v):
                if (Graph.adj[vis][i] == 1 and
                      (not visited[i])):
                    q.append(i)
                    visited[i] = True
v, e = 7,8
G = Graph(v, e)
G.addEdge(0, 1)
G.addEdge(0, 2)
G.addEdge(1, 3)
G.BFS(0)