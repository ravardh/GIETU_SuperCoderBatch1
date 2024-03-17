class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs_tree(root):
    if not root:
        return

    queue = [root]
    while queue:
        current_node = queue.pop(0)
        print(current_node.value, end=" ")

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)


root = Node(15)
root.left = Node(26)
root.right = Node(33)
root.left.left = Node(43)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

print("BFS of the tree:")
bfs_tree(root)
