import heapq
def dijkstra(graph, start, end):
    # Initialize the priority queue and distances 
    queue = [(0, start)]
    distances = {node: float('infinity') for node in range(len(graph))}
    distances[start] = 0
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in enumerate(graph[current_node]):
            if weight == 0:
                continue
            tentative_distance = current_distance + weight

            # If  tentative distance is smaller than  current distance, update  distance ,add neighbor to  queue
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                heapq.heappush(queue, (tentative_distance, neighbor))

    # Return  distance, shortest path
    path = []
    while end != start:
        path.append(end)
        end = next(node for node, dist in enumerate(distances) if dist > 0 and dist < distances[end] and graph[node][end] != 0)
    path.append(start)
    return distances[end], path[::-1]
start = int(input("Enter the starting node: "))
end = int(input("Enter the ending node: "))
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 11],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 0],
    [0, 11, 2, 0, 0, 0, 6, 0, 0]
]
distance, path = dijkstra(graph, start, end)
print("Shortest path:", path)