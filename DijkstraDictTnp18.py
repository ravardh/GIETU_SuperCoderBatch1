def dijkstra(graph, start):

    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    visited = set()

    while len(visited) < len(graph):
        current_vertex = min((v for v in graph if v not in visited), key=distances.get)
        visited.add(current_vertex)
        for neighbor, weight in graph[current_vertex].items():
            if distances[current_vertex] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_vertex] + weight

    return distances

graph = {
    '1': {'2': 4, '8': 8},
    '2': {'3': 8, '8': 11, '1':4},
    '3': {'4': 7, '9': 2, '6': 4,'2': 8},
    '4': {'5': 9, '6': 14,'3': 7},
    '5': {'6': 10,'4': 9},
    '6': {'7': 2,'5': 10,'4': 14,'3': 4},
    '7': {'8': 1, '9': 6,'6': 2},
    '8': {'9': 7,'7': 1,'1': 8,'2': 11},
    '9': {'3': 2, '8': 7,'7': 6}
}
source_vertex = '1'
shortest_distances = dijkstra(graph, source_vertex)

print("Vertex \t Distance from Source")
for vertex, distance in shortest_distances.items():
    print(f"{vertex} \t {distance}")
