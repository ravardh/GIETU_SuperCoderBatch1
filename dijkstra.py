def shortest_paths(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    unvisited = list(graph.keys())

    while unvisited:
        def get_distance(node):
            return distances[node]

        min_distance_node = min(unvisited, key=get_distance)
        unvisited.remove(min_distance_node)

        for neighbor, weight in graph[min_distance_node].items():
            distance = distances[min_distance_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = min_distance_node

    return distances, previous_nodes

def print_shortest_paths(start, distances, previous_nodes):
    for node, distance in distances.items():
        if node != start:
            path = [node]
            current_node = node
            while previous_nodes[current_node] is not None:
                path.insert(0, previous_nodes[current_node])
                current_node = previous_nodes[current_node]
            print(f"The shortest path from node {start} to node {node} is: {path}, Distance: {distance}")

graph = {
    '1': {'2': 4, '8': 8},
    '2': {'1': 4, '8': 4, '3': 8},
    '3': {'2': 8, '9': 2, '6': 4, '4': 7},
    '4': {'3': 7, '6': 14, '5': 9},
    '5': {'4': 9, '6': 10},
    '6': {'4': 14, '3': 4, '5': 10, '7': 2},
    '7': {'6': 2, '9': 6, '8': 1},
    '9': {'3': 2, '7': 6, '8': 7},
    '8': {'1': 8, '2': 4, '9': 7, '7': 1},
}

start_node = '3'
distances, previous_nodes = shortest_paths(graph, start_node)
print("Shortest distances from node", start_node + ":")
print_shortest_paths(start_node, distances, previous_nodes)
