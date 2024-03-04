class TreeNode:
    def __init__(self, val=0, left=None, right=None):
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
            if i == 0: 
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

print(level1)
print(left_side_view(root))


#approach 2
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def first_elements_of_levels(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_vals = []
        for i in range(level_size):
            node = queue.popleft()
            if i == 0:
                level_vals.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if level_vals: 
            result.append(level_vals[0])

    return result

# Constructing the binary tree
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

print(first_elements_of_levels(root))