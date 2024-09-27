class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, w))
        #self.graph[v].append((u, w))

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        pq = [(0, start)]

        while pq:
            current_distance, current_node = pq.pop(0)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph.get(current_node, []):
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    pq.append((distance, neighbor))

        return distances

# Example usage
g = Graph()
g.addEdge('1', '2', 4)
g.addEdge('2', '1', 4)

g.addEdge('1', '8', 8)
g.addEdge('8', '1', 8)

g.addEdge('3', '2', 8)
g.addEdge('2', '3', 8)

g.addEdge('2', '8', 11)
g.addEdge('8', '2', 11)

g.addEdge('8', '7', 1)
g.addEdge('7', '8', 1)

g.addEdge('9', '8', 7)
g.addEdge('8', '9', 7)

g.addEdge('3', '9', 2)
g.addEdge('9', '3', 2)

g.addEdge('3', '4', 7)
g.addEdge('4', '3', 7)

g.addEdge('3', '6', 4)
g.addEdge('6', '3', 4)

g.addEdge('5', '4', 9)
g.addEdge('4', '5', 9)

g.addEdge('4', '6', 14)
g.addEdge('6', '4', 14)

g.addEdge('5', '6', 10)
g.addEdge('6', '5', 10)

g.addEdge('7', '9', 6)
g.addEdge('9', '7', 6)

g.addEdge('6', '7', 2)
g.addEdge('7', '6', 2)

start_node = '3'
distances = g.dijkstra(start_node)

for node, distance in distances.items():
    print(f"Distance from {start_node} to {node}: {distance}")
