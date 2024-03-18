import heapq

def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]

def union(parent, rank, u, v):
    u_root = find(parent, u)
    v_root = find(parent, v)
    if rank[u_root] < rank[v_root]:
        parent[u_root] = v_root
    elif rank[u_root] > rank[v_root]:
        parent[v_root] = u_root
    else:
        parent[v_root] = u_root
        rank[u_root] += 1

def kruskal(graph):
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            edges.append((weight, vertex, neighbor))
    
    edges.sort()  # Sort edges by weight
    min_spanning_tree = []
    parent = {vertex: vertex for vertex in graph}
    rank = {vertex: 0 for vertex in graph}

    for weight, src, dest in edges:
        if find(parent, src) != find(parent, dest):
            min_spanning_tree.append((weight, src, dest))
            union(parent, rank, src, dest)

    return min_spanning_tree

graph = {
    '1': [('2', 6), ('3', 5), ('5', 4)],
    '5': [('1', 4), ('4', 1), ('6', 8)],
    '6': [('5', 8), ('4', 7)],
    '4': [('3', 3), ('5', 1), ('8', 10), ('6', 7)],
    '8': [('4', 10), ('7', 9)],
    '7': [('3', 11), ('8', 9)],
    '3': [('1', 5), ('4', 3), ('7', 11), ('2', 2)],
    '2': [('1', 6), ('3', 2)],
}

min_spanning_tree = kruskal(graph)
print("Minimum Spanning Tree:")
for weight, src, dest in min_spanning_tree:
    print(f"Edge: {src}-{dest} Weight: {weight}")
o 