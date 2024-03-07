# DFS algorithm in Python
#11,7,3,2,1,10,8,9,6,5,4,

# DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['11', '7','4','5']),
         '1': set(['3','8','2', '4']),
         '2': set(['1','10']),
         '3': set(['7','1']),
         '4': set(['8', '9'])}

dfs(graph, '0')
