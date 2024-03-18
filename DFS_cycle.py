def DFS_cycle(start, graph, visited, parent):
    visited[start - 1] = True

    for i in graph[start - 1]:
        if not visited[i[1] - 1]:
            parent[i[1] - 1] = start
            if DFS_cycle(i[1], graph, visited, parent):
                return True
        elif parent[start - 1] != i[1]:
            return True

    return False


def has_cycle(graph):
    v = len(graph)
    visited = [False] * v
    parent = [-1] * v

    for i in range(v):
        if not visited[i]:
            if DFS_cycle(i + 1, graph, visited, parent):
                return True

    return False

def create_graph(graph,source,destination,weight=1):
    graph[source-1].append((source,destination,weight))

v = 2  #11
graph = [[] for _ in range(v)]

create_graph(graph, 1, 2)
create_graph(graph, 2, 1)

# create_graph(graph, 1, 2)
# create_graph(graph, 1, 3)
# create_graph(graph, 1, 10)
# create_graph(graph, 2, 1)
# create_graph(graph, 2, 4)
# create_graph(graph, 3, 1)
# create_graph(graph, 3, 7)
# create_graph(graph, 4, 2)
# create_graph(graph, 4, 5)
# create_graph(graph, 4, 7)
# create_graph(graph, 4, 8)
# create_graph(graph, 5, 4)
# create_graph(graph, 5, 6)
# create_graph(graph, 6, 5)
# create_graph(graph, 6, 10)
# create_graph(graph, 6, 9)
# create_graph(graph, 7, 3)
# create_graph(graph, 7, 4)
# create_graph(graph, 7, 11)
# create_graph(graph, 8, 4)
# create_graph(graph, 8, 9)
# create_graph(graph, 9, 6)
# create_graph(graph, 9, 8)
# create_graph(graph, 10, 1)
# create_graph(graph, 10, 6)
# create_graph(graph, 11, 7)

print(graph)
print("Does the graph contain a cycle?", has_cycle(graph))
