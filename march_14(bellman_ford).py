#bellman_ford
def bellman_ford(graph, src):
    distance = {}
    
    for vertex in graph:
        distance[vertex] = float('inf')

    distance[src] = 0

    for i in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

    return distance

graph = {
    1: [(2, 6), (3, 5), (4, 5)],
    2: [(5, -1)],
    3: [(2, -2), (5, 1)],
    4: [(3, -2), (6, -1)],
    5: [(7, 3)],
    6: [(7, 3)],
    7: []
}

source = 1

shortest_distances = bellman_ford(graph, source)
print("Shortest distance from", source)

for node, distance in shortest_distances.items():
    print(node, ":", distance)
