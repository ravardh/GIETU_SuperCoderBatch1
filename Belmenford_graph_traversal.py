def bellman_ford(nodes, edges, start):
    edge_list = {node: ([], []) for node in nodes}
    for node1, node2, weight in edges:
        edge_list[node1][0].append((node2, weight)) 
        edge_list[node2][1].append((node1, weight)) 

    distances = {node: float('inf') for node in nodes}
    distances[start] = 0

    for _ in range(len(nodes) - 1):      # running the loop for n-1 times over all vertex
        for node, (outgoing_edges, _) in edge_list.items():
            for neighbor, weight in outgoing_edges:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Check for negative cycles
    for node, (outgoing_edges, _) in edge_list.items():
        for neighbor, weight in outgoing_edges:
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative cycle")

    return distances

nodes = ['1', '2', '3', '4', '5', '6', '7']
edges = [
    ('1', '2', 6), 
    ('1', '3', 5),
    ('1', '4', 5),
    ('2', '5', -1),
    ('3', '2', -2),
    ('3', '5', 1),  
    ('4', '3', -2), 
    ('4', '6', -1),
    ('5', '7', 3),
    ('6', '7', 3),
]

start_node = '1'
shortest_distances = bellman_ford(nodes, edges, start_node)
print("Shortest distances from node", start_node + ":")
for node, distance in shortest_distances.items():
    print("Node:", node, "Distance:", distance)
