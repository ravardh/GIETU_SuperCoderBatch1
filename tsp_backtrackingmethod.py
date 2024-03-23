'''def tsp(graph, start):
    n = len(graph)
    visited = [False] * n
    visited[start] = True
    min_cost = float('inf')

    def dfs(node, depth, cost):
        nonlocal min_cost
        if depth == n - 1:
            return cost + graph[node][start] 
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                min_cost = min(min_cost, dfs(i, depth + 1, cost + graph[node][i]))
                visited[i] = False
        return min_cost

    return dfs(start, 0, 0)

if __name__ == "__main__":
    graph = [
        [0, 10, 15, 20],
        [5, 0, 9, 10],
        [6, 13, 0, 12],
        [8, 8, 9, 0]
    ]
    start_node = 0
    min_cost = tsp(graph, start_node)
    print("Minimum cost of traversal:", min_cost)'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

def construct_tree(graph, root):
    n = len(graph)
    tree = [TreeNode(i) for i in range(n)]
    visited = [False] * n
    visited[root] = True

    while False in visited:
        min_weight = float('inf')
        min_index = None
        for i in range(n):
            if not visited[i] and graph[root][i] < min_weight:
                min_weight = graph[root][i]
                min_index = i
        tree[root].children.append(tree[min_index])
        tree[min_index].parent = tree[root]
        visited[min_index] = True
        root = min_index

    return tree

def tsp_tree(root_node):
    min_cost = float('inf')

    def dfs(node, parent, cost):
        nonlocal min_cost
        if not node:
            return 0
        if len(node.children) == 0:
            return cost + node.value
        for child in node.children:
            if child != parent:
                min_cost = min(min_cost, dfs(child, node, cost + node.value))
        return min_cost

    return dfs(root_node, None, 0)

# Given graph
graph = [
    [0, 10, 15, 20],
    [5, 0, 9, 10],
    [6, 13, 0, 12],
    [8, 8, 9, 0]
]
root_node = 0

# Construct tree from the graph
tree = construct_tree(graph, root_node)

# Solve TSP on the tree
min_cost = tsp_tree(tree[root_node])
print("Minimum cost of traversal in the tree:", min_cost)
