from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Assuming an undirected graph

    def bfs(self, start):
        visited = set()
        result_bfs = []
        queue = deque([start])

        while queue:
            current_vertex = queue.popleft()
            if current_vertex not in visited:
                result_bfs.append(current_vertex)
                visited.add(current_vertex)
                queue.extend(self.graph[current_vertex])

        return result_bfs

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        result_dfs = []

        if start not in visited:
            result_dfs.append(start)
            visited.add(start)
            for neighbor in self.graph[start]:
                result_dfs.extend(self.dfs(neighbor, visited))

        return result_dfs

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

start_vertex = 1

# BFS
bfs_result = g.bfs(start_vertex)
print(f"BFS traversal starting from vertex {start_vertex}: {bfs_result}")

# DFS
dfs_result = g.dfs(start_vertex)
print(f"DFS traversal starting from vertex {start_vertex}: {dfs_result}")
