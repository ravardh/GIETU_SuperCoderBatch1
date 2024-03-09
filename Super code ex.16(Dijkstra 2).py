import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def minimum_path(graph, start, destination):
    distances = dijkstra(graph, start)
    return distances[destination]
graph = {
    'A': {'B': 4, 'C': 8},
    'B': {'A': 4, 'C': 4, 'D': 8},
    'C': {'A': 8, 'B': 4, 'F': 1, 'E': 7},
    'D': {'B': 8, 'E': 2, 'G': 7, 'H': 14},
    'E': {'C': 7, 'D': 2, 'F': 6},
    'F': {'C': 1, 'H': 2, 'E': 6},
    'G': {'D': 7, 'H': 14, 'I': 9},
    'H': {'D': 4, 'F': 2, 'G': 14, 'I': 10},
    'I': {'G': 9, 'H': 10}
}

start_vertex = 'A'
destination_vertex = 'I'

min_distance = minimum_path(graph, start_vertex, destination_vertex)
print(f"The minimum distance from {start_vertex} to {destination_vertex} is {min_distance}")

