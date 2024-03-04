class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = set()
        if v not in self.adj_list:
            self.adj_list[v] = set()
        self.adj_list[u].add(v)
        self.adj_list[v].add(u)

    def dfs(self, node, visited):
        visited.add(node)
        print(node, end=" ")  # Process the current node

        for neighbor in self.adj_list.get(node, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(5, 3)
    graph.add_edge(5, 8)
    graph.add_edge(3, 6)
    graph.add_edge(3, 7)
    graph.add_edge(8, 4)

    start_node = 5
    visited_nodes = set()
    print("DFS traversal starting from vertex", start_node)
    graph.dfs(start_node, visited_nodes)
