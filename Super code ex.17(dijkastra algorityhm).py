def shortest_paths(nodes, edges, start):
    distances = {node: float('inf') for node in nodes}
    distances[start] = 0
    visited = set()
    while len(visited) < len(nodes):
        min_node = None
        min_distance = float('inf')
        for node in nodes:
            if node not in visited and distances[node] < min_distance:
                min_node = node
                min_distance = distances[node]
        visited.add(min_node)
        for edge in edges:
            node1, node2, weight = edge
            if node1 == min_node and node2 in nodes:
                distances[node2] = min(distances[node2], distances[node1] + weight)
            elif node2 == min_node and node1 in nodes:
                distances[node1] = min(distances[node1], distances[node2] + weight)

    return distances
nodes = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
edges = [
    ('1', '2', 4), 
    ('1', '8', 8),
    ('2', '8', 4), 
    ('2', '3', 8),
    ('3', '9', 2), 
    ('3', '6', 4), 
    ('3', '4', 7),
    ('4', '6', 14), 
    ('4', '5', 9),
    ('5', '6', 10),
    ('6', '7', 2),
    ('7', '9', 6), 
    ('7', '8', 1),
    ('8', '9', 7)
]

start_node = '3'
shortest_distances = shortest_paths(nodes, edges, start_node)
print("Shortest distances from node", start_node + ":")
for node, distance in shortest_distances.items():
    print("Node:", node, "Distance:",distance)
