def dfs(strt, visit, parent):
    print(strt)
    visit[strt - 1] = True

    for n in graph[strt - 1]:
        if not visit[n[1] - 1]:
            parent[n[1] - 1] = strt
            dfs(n[1], visit, parent)
        elif parent[strt - 1] != n[1]:
            print("Cycle detected:", n[1], "->", strt)

def create_graph(graph, src, dst):
    graph[src - 1].append((src, dst))

v = 7
graph = [[] for _ in range(v)]

for i in range(v):                                                                                                                                                                                                                  
    graph[i] = []

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

print(graph)

visit = [False] * len(graph)
parent = [-1] * len(graph)
dfs(1, visit, parent)
