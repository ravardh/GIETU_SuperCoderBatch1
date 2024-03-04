# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    if not root:
        return []

    result = []
    level_nodes = [root]

    while level_nodes:
        result.append(level_nodes[-1].val)
        next_level_nodes = []

        for node in level_nodes:
            if node.left:
                next_level_nodes.append(node.left)
            if node.right:
                next_level_nodes.append(node.right)

        level_nodes = next_level_nodes

    return result

# Example usage:
# Create a binary tree

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

print(rightSideView(root))  
