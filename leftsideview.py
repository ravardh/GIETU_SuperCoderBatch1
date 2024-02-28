class TreeNode:
    def _init_(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_side_view(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.pop(0)
            if i == 0:  # First node in the level (leftmost node)
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result

root = TreeNode(9)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.right = TreeNode(4)
root.left.left = TreeNode(6)
root.left.left.right = TreeNode(5)
root.right.left = TreeNode(3)
root.right.left.left = TreeNode(11)
root.right.right = TreeNode(2)
root.right.left.right = TreeNode(12)
root.right.left.right.right = TreeNode(17)

print(left_side_view(root))
