'''
#with use of priority queue and graph 
class PriorityQueue:
    def __init__(self):
        self.queue =[]

    def push(self, item):
        self.queue.append(item)
        self.queue.sort()

    def pop(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

def shortest_paths(graph,start):
    distances={node:float('inf')for node in graph}
    distances[start] =0
    priority_queue= PriorityQueue()
    priority_queue.push((0,start))

    while not priority_queue.is_empty():
        current_distance,current_node=priority_queue.pop()
        if current_distance>distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                priority_queue.push((distance, neighbor))
    
    return distances
# adjacency list
graph = {
    '1':{'2':4,'8':8},
    '2':{'1':4,'8':4,'3':8},
    '3':{'2':8,'9':2,'6':4,'4':7},
    '4':{'3':7,'6':14,'5':9},
    '5':{'4': 9, '6': 10},
    '6':{'4':14,'3':4,'5':10,'7':2},
    '7':{'6':2,'9':6,'8':1},
    '9':{'3':2,'7':6,'8':7},
    '8':{'1':8,'2':4,'9':7,'7':1},
}

start_node='3'
shortest_distances=shortest_paths(graph,start_node)
print("Shortest distances from node",start_node+":")
for node, distance in shortest_distances.items():
    print("Node:",node,"Distance:",distance)'''

#with the use of adjecency list use 
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
    print("Node:", node, "Distance:", distance)
