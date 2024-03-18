def create_graph(graph, src, dst):
    graph[src - 1].append(dst)
    graph[dst - 1].append(src)  

def bfs(start):
    visited = [False] * len(graph)
    queue = []

    visited[start - 1] = True
    queue.append(start)

    while queue:
        nod = queue.pop(0)
        print(nod, end=" ")

        for i in graph[nod - 1]:
            if not visited[i - 1]:
                visited[i - 1] = True
                queue.append(i)


v = 5 
graph = [[] for _ in range(v)]

create_graph(graph, 1, 2)
create_graph(graph, 1, 3)
create_graph(graph, 1, 4)
create_graph(graph, 2, 4)
create_graph(graph, 3, 5)
create_graph(graph, 3, 2)
create_graph(graph, 4, 1)
create_graph(graph, 4, 2)
create_graph(graph, 5, 3)

print("Following is the Breadth-First Search:")
bfs(1)

