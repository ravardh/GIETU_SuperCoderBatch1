class Graph:
    def __init__(self):
        self.graph = []  # i use list to store edges for pair of vertices 

    def add_edge(self, u, v):
        self.graph.append((u, v))  # i just joined  an edge (u, v) to the list
        self.graph.append((v, u))  # i am taking  it as a undirected graph

    def bfs(self, start):
        visited = set()
        result_bfs = []
        queue = [start]

        while queue:
            current_vertex = queue.pop(0)
            if current_vertex not in visited:
                result_bfs.append(current_vertex)
                visited.add(current_vertex)
                for u, v in self.graph:
                    if u == current_vertex:
                        queue.append(v)

        return result_bfs

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        result_dfs = []

        if start not in visited:
            result_dfs.append(start)
            visited.add(start)
            for u, v in self.graph:
                if u == start:
                    result_dfs.extend(self.dfs(v, visited))

        return result_dfs

# example of nodes usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

start_vertex = 1

# Breadth first search codnition  i have taken 
bfs_result = g.bfs(start_vertex)
print(f"BFS traversal starting from vertex {start_vertex}: {bfs_result}")

# DFS taken
dfs_result = g.dfs(start_vertex)
print(f"DFS traversal starting from vertex {start_vertex}: {dfs_result}")
