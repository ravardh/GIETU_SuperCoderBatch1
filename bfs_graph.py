class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.adj_list = [[] for _ in range(vertex)]
        self.visited = set()

    def add_edge(self, r, s):
        self.adj_list[r-1].append((r, s))

    def bfs(self, start):
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in self.visited:
                print(node, end=" ")
                self.visited.add(node)
            for edge in self.adj_list[node-1]:
                    x = edge[1]
                    if x not in self.visited:
                        queue.append(x)

graph = Graph(9)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 9)
graph.add_edge(2, 4)
graph.add_edge(2, 1)
graph.add_edge(3, 1)
graph.add_edge(3, 8)
graph.add_edge(4, 5)
graph.add_edge(4, 6)
graph.add_edge(4, 2)
graph.add_edge(5, 4)
graph.add_edge(6, 4)
graph.add_edge(6, 7)
graph.add_edge(7, 6)
graph.add_edge(7, 8)
graph.add_edge(8, 3)
graph.add_edge(8, 9)
graph.add_edge(9, 1)
graph.add_edge(9, 8)

graph.bfs(1)

'''from collections import defaultdict

def add_edge(adj_list, u, v):
    adj_list[u].append(v)
    adj_list[v].append(u) 

def create_adjacency_list(edges):
    adj_list = defaultdict(list)
    for edge in edges:
        u, v = edge
        add_edge(adj_list, u, v)
    return adj_list

def bfs(adj_list, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend([n for n in adj_list[node] if n not in visited])

edges = [(1, 2), (1, 3), (1, 9), (2, 4), (2, 1), (3, 1),(3,8),(4,2),(4,5),(4,6),(5,4),(6,4),(6,7),(7,6),(7,8),(8,7),(8,3),(8,9),(9,8),(9,1)]
adj_list = create_adjacency_list(edges)
#print("Adjacency List:", adj_list)
print("Following is a BFS search operation:")
bfs(adj_list,1)'''