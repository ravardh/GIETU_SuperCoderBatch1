class Graph:
    def __init__(self,v):
        self.v = v
        self.adj_list=[[] for _ in range(v)]
        self.visited=set()

    def add_edge(self,s,d,w):
        self.adj_list[s].append((s,d,w))
        self.adj_list[d].append((d,s,w))

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def kruskal_mst(graph):
    result = []
    i = 0
    e = 0
    graph.adj_list.sort(key=lambda x: x[2])

    parent = []
    rank = []

    for node in range(graph.v):
        parent.append(node)
        rank.append(0)

    while e < graph.v - 1:
        s, d, w = graph.adj_list[i]
        i += 1
        x = find(parent, s - 1)
        y = find(parent, d - 1)

        if x != y:
            e += 1
            result.append((s, d, w))
            union(parent, rank, x, y)

    return result

g = Graph(4)
g.add_edge(1, 2, 10)
g.add_edge(1, 3, 20)
g.add_edge(2, 3, 30)
g.add_edge(2, 4, 5)

mst = kruskal_mst(g)
total_weight = sum(edge[2] for edge in mst)

print("Edges of Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total weight of Minimum Spanning Tree:", total_weight)
