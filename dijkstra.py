def dijkstra(adj_list, start):
    num_nodes = len(adj_list)
    distances = [float('inf')] * num_nodes
    distances[start] = 0

    visited = [False] * num_nodes

    for _ in range(num_nodes):
        min_distance = float('inf')
        min_node = None
        for node in range(num_nodes):
            if not visited[node] and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node

        if min_node is None:
            break

        visited[min_node] = True

        for neighbor, weight in adj_list[min_node]:
            new_distance = distances[min_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances

if __name__ == "__main__":
    graph = {
        0: [(1, 4), (7, 8)],
        1: [(2, 8), (7, 11)],
        2: [(1, 8), (3, 7), (5, 4), (8, 2)],
        3: [(2, 7), (4, 9), (5, 14)],
        4: [(3, 9), (5, 10)],
        5: [(4, 10), (3, 4), (6, 2)],
        6: [(5, 2), (7, 6), (8, 1)],
        7: [(0, 8), (1, 11), (6, 7)],
        8: [(2, 2), (6, 1), (9, 7)],
        9: [(8, 7), (6, 6), (7, 1)]
    }

    start_node = 0
    shortest_distances = dijkstra(graph, start_node)

    print("Shortest distances from node", start_node)
    for node, distance in enumerate(shortest_distances):
        print(f"Node {node}: Distance={distance}")