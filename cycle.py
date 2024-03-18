def create_graph(graph, src, dst):
    graph[src - 1].append(dst)
    graph[dst - 1].append(src)  

def bfs(start):
    visited = [False] * len(graph)
    queue = []
    parent = [-1] * len(graph)  

    visited[start - 1] = True
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for n in graph[node - 1]:
            if not visited[n - 1]:
                visited[n - 1] = True
                parent[n - 1] = node  
                queue.append(n)
            elif parent[node - 1] != n:  
                print("\nCycle detected at node:", n)
                return

v = 7
graph = [[] for _ in range(v)]

create_graph(graph, 1, 2)
create_graph(graph, 1, 3)
create_graph(graph, 2, 1)
create_graph(graph, 2, 4)
create_graph(graph, 3, 1)
create_graph(graph, 3, 4)
create_graph(graph, 3, 5)
create_graph(graph, 4, 2)
create_graph(graph, 5, 3)
create_graph(graph, 5, 3)
create_graph(graph, 5, 6)
create_graph(graph, 6, 5)
create_graph(graph, 6, 7)
create_graph(graph, 7, 6)


print("Following is the Breadth-First Search:")
bfs(1)
