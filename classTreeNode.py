class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightView(root):
    if not root:
        return []

    right_view = []
    queue = [(root, 0)]  
    while queue:
        node, level = queue.pop(0)

        if len(right_view) == level:
            right_view.append(node.val)

        if node.right:
            queue.append((node.right, level + 1))

        if node.left:
            queue.append((node.left, level + 1))

    return right_view

root = TreeNode(9)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(2)
root.left.left.right = TreeNode(5)
root.right.left.left = TreeNode(11)
root.right.left.right = TreeNode(12)

root.right.left.right.right = TreeNode(17)

print("Right view of the tree:", rightView(root))