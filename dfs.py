class Graph:
    def __init__(self):
        self.graph = {}  # Initialize an empty adjacency list

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)  # Add an edge (u, v) to the adjacency list

    def dfs(self, node, visited=None):
        if visited is None:
            visited = set()
        visited.add(node)
        print(node, end=" ")  # Print the visited node

        for neighbor in self.graph.get(node, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

start_vertex = 2
print("DFS traversal starting from vertex", start_vertex)
g.dfs(start_vertex)
