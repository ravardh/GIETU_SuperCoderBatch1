def bfs(graph, start):
    visited = set()  
    queue = []  

    queue.append(start)  
    visited.add(start)  

    while queue:
        current_vertex = queue.pop(0)  
        print(current_vertex, end=" ")  

        # Explore adjacent vertices
        for neighbor in graph.get(current_vertex, []):
            if neighbor not in visited:
                queue.append(neighbor)  
                visited.add(neighbor) 
if __name__ == "__main__":
    
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'G'}
    }

    start_vertex = 'A'
    print("BFS traversal starting from vertex", start_vertex)
    bfs(graph, start_vertex)
