class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert(self, value):
        self._insert_recursively(self.root, value)

    def _insert_recursively(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert_recursively(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._insert_recursively(current_node.right, value)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

if __name__ == "__main__":
    # Create a binary tree and insert elements
    binary_tree = BinaryTree(5)
    binary_tree.insert(12)
    binary_tree.insert(18)
    binary_tree.insert(10)
    binary_tree.insert(14)
    binary_tree.insert(26)
    binary_tree.insert(22)

    # Perform an inorder traversal to display the elements
    print("Inorder Traversal:")
    binary_tree.inorder_traversal(binary_tree.root)
