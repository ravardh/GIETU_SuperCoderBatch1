def create_graph(graph, src, dst):
    graph[src - 1].append(dst)
    graph[dst - 1].append(src)  

def bfs(graph, start):
    visited = [False] * len(graph)
    queue = []

    visited[start - 1] = True
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbour in graph[node - 1]:
            if not visited[neighbour - 1]:
                visited[neighbour - 1] = True
                queue.append(neighbour)


v = 9 
graph = [[] for _ in range(v)]

create_graph(graph, 1, 2)
create_graph(graph, 1, 3)
create_graph(graph, 1, 9)
create_graph(graph, 2, 4)
create_graph(graph, 3, 5)
create_graph(graph, 3, 7)
create_graph(graph, 4, 1)
create_graph(graph, 4, 2)
create_graph(graph, 5, 3)

print("Following is the Breadth-First Search:")
bfs(graph, 1)