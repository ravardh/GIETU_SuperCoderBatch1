def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    unvisited = graph.copy()

    while unvisited:
        current_node = min(unvisited, key=lambda node: distances[node])
        unvisited.pop(current_node)

        for neighbor, weight in graph[current_node]:
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_node

    paths = {}
    for end_node in distances:
        path, current_node = [], end_node
        while previous_nodes[current_node] is not None:
            path.insert(0, current_node)
            current_node = previous_nodes[current_node]
        if path:
            path.insert(0, current_node)
        paths[end_node] = path

    return distances, paths

graph = {
    1: [(2, 4), (8, 8)],
    2: [(3, 8), (8, 11)],
    3: [(2, 8), (4, 7), (6, 4), (9, 2)],
    4: [(3, 7), (5, 9), (6, 14)],
    5: [(4, 9), (6, 10)],
    6: [(5, 10), (3, 4), (7, 2)],
    7: [(6, 2), (9, 6), (8, 1)],
    8: [(1, 8), (2, 11), (9, 7)],
    9: [(8, 7), (3, 2), (7, 6)]
}

start = int(input("Enter the start node: "))
distances, paths = dijkstra(graph, start)

print(f"Shortest distances from node {start}:")
for node, distance in distances.items():
    print(f"Node {node}: Distance = {distance}, Path = {paths[node]}")
