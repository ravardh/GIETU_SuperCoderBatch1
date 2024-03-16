
def dijkstra(graph, src):
    dist = {}
    
    for node in graph:
        dist[node] = float('inf')
        
    dist[src] = 0
    visited = []

    while len(visited) < len(graph):
        u = None
        
        for node in graph:
            if node not in visited:
                if u is None or dist[node] < dist[u]:
                    u = node
        visited.append(u)

        for v, weight in graph[u].items():
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    return dist


graph = {
    1: {2: 4, 8: 8},
    2: {1: 4, 3: 8, 8: 11},
    3: {2: 8, 4: 7, 6: 4, 9: 2},
    4: {3: 7, 5: 9, 6: 14},
    5: {4: 9, 6: 10},
    6: {3: 4, 4: 14, 5: 10, 7: 2},
    7: {6: 2, 8: 1, 9: 6},
    8: {1: 8, 2: 11, 7: 1, 9: 7},
    9: {3: 2, 7: 6, 8: 7},
}

source = 3
shortest_distances = dijkstra(graph, source)

print("Shortest distances from", source)

for node, distance in shortest_distances.items():
    print(node, ":", distance)
