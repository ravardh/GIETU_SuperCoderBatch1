class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def addedge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(node):
        stack = list()
        visited_list = list()
        stack.append(node)
        visited_list.append(node)
        while stack:
            vertex = stack.pop()
            print(vertex, end=" ")
            for u in graph[vertex]:
                if u not in visited_list:
                    stack.append(u)
                    visited_list.append(u)

# Example usage
vertices = 5
g = Graph(vertices)
g.addedge(0, 1)
g.addedge(0, 2)
g.addedge(1, 2)
g.addedge(2, 3)
g.addedge(3, 4)

print("DFS traversal from node 0:")
g.dfs()
