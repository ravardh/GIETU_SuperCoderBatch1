class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

# Example usage:
if __name__ == "__main__":
    root = None
    keys = [5, 3, 7, 2, 4, 6, 8]

    for key in keys:
        root = insert(root, key)

    # Print the inorder traversal of the BST
    inorder_traversal(root)

