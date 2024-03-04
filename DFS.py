def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=' ')

    start_index = start

    for i, connected in enumerate(graph[start_index]):
        if connected == 1 and i not in visited:
            dfs(graph, i, visited)


graph = [
    [0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0]
]

print("DFS Traversal:")
dfs(graph, 0)
