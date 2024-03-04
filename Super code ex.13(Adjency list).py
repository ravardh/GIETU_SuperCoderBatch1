#creating a adjency list using python in graph
class Graph:
    def __init__(self):
        self.adj_list = {}  # Initialize an empty dictionary

    def add_edge(self, u, v):
        # Add an edge between vertices u and v
        if u not in self.adj_list:
            self.adj_list[u] = set()
        if v not in self.adj_list:
            self.adj_list[v] = set()
        self.adj_list[u].add(v)
        self.adj_list[v].add(u)  # Since it's an undirected graph

# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'F')

    # Print the adjacency list
    for vertex, neighbors in graph.adj_list.items():
        print(f"{vertex}: {neighbors}")
