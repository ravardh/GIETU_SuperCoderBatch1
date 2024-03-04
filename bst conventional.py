class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_bst(root, val):
    if not root:
        return Node(val)

    current = root
    while True:
        if val < current.val:
            if not current.left:
                current.left = Node(val)
                break
            current = current.left
        else:
            if not current.right:
                current.right = Node(val)
                break
            current = current.right

    return root

def inorder_traversal(root):
    stack, inorder = [], []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        inorder.append(current.val)
        current = current.right

    return inorder

# Create an empty tree
root = None

# Insert nodes into the tree
root = insert_bst(root, 10)
root = insert_bst(root, 5)
root = insert_bst(root, 15)
root = insert_bst(root, 2)
root = insert_bst(root, 7)
root = insert_bst(root, 12)
root = insert_bst(root, 17)

# Traverse the tree in an inorder manner
inorder = inorder_traversal(root)
print(inorder)