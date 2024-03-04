from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.hd = 0

def find_leaf_nodes(root):
    if root is None:
        return []

    if root.left is None and root.right is None:
        return [root.data]

    left_leaf_nodes = find_leaf_nodes(root.left)
    right_leaf_nodes = find_leaf_nodes(root.right)

    return left_leaf_nodes + right_leaf_nodes

def print_top_view(root):
    if root is None:
        return

    queue = deque()
    m = dict()
    hd = 0

    root.hd = hd
    queue.append(root)

    while queue:
        node = queue.popleft()
        hd = node.hd

        if hd not in m:
            m[hd] = node.data

        if node.left:
            node.left.hd = hd - 1
            queue.append(node.left)

        if node.right:
            node.right.hd = hd + 1
            queue.append(node.right)

    for i in sorted(m):
        print(m[i], end=" ")

def print_bottom_view(root):
    if root is None:
        return

    queue = deque()
    m = dict()
    hd = 0

    root.hd = hd
    queue.append(root)

    while queue:
        node = queue.popleft()
        hd = node.hd

        m[hd] = node.data

        if node.left:
            node.left.hd = hd - 1
            queue.append(node.left)

        if node.right:
            node.right.hd = hd + 1
            queue.append(node.right)

    for i in sorted(m):
        print(m[i], end=" ")

def print_left_view(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            if i == 0:
                print(node.data, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

def print_right_view(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            if i == size - 1:
                print(node.data, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)



root = Node(10)
root.left = Node(9)
root.right = Node(14)
root.left.left = Node(5)
root.left.left.left=Node(2)
root.left.left.right=Node(7)
root.left.left.left.right=Node(3)
root.left.left.right.right=Node(8)
root.right.left = Node(12)
root.right.right = Node(17)
root.right.right.leftt=Node(15)



# Execute the functions
leaf_nodes = find_leaf_nodes(root)
print("\nLeaf nodes are:", leaf_nodes)

print("\nTop view nodes are:")
print_top_view(root)

print("\n\nBottom view nodes are:")
print_bottom_view(root)

print("\n\nLeft view nodes are:")
print_left_view(root)

print("\n\nRight view nodes are:")
print_right_view(root)