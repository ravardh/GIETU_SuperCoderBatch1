#LEFT NODE
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leftView(root):
    if not root:
        return []

    left_view = []
    queue = [(root, 0)]  

    while queue:
        node, level = queue.pop(0)

        if len(left_view) == level:
            left_view.append(node.val)

        if node.left:
            queue.append((node.left, level + 1))

        if node.right:
            queue.append((node.right, level + 1))

    return left_view

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

print("Left view of the tree:", leftView(root))


#RIGHT NODE
class TreeNode:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None

def right_view(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            current_node = queue.pop(0)

            if i == level_size - 1:
                result.append(current_node.data)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

print(right_view(root))