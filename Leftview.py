class TreeNode:
    def _init_(self, val):
        self.val = val
        self.left = None
        self.right = None


def leftViewUtil(root, level, max_level, result):
    if root is None:
        return

  
    if (max_level[0] < level):
        result.append(root.val)
        max_level[0] = level

   
    leftViewUtil(root.left, level + 1, max_level, result)
    leftViewUtil(root.right, level + 1, max_level, result)


def leftView(root):
    result = []
    max_level = [0]  
    leftViewUtil(root, 1, max_level, result)
    return result



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left

print("Left view of binary tree:")
print(leftView(root))
