'''class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def constructBST(nums):
    if not nums:
        return None
    root = None
    for num in nums:
        root = insert(root, num)
    return root

def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val, end=' ')
        inorderTraversal(root.right)

# Example usage:
arr = [8, 3, 10, 1, 6, 14, 4, 7, 13]
root = constructBST(arr)
print("Inorder Traversal of constructed BST:")
inorderTraversal(root)'''


class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def insert_into_tree(arr):
    if not arr:
        return None
    
    root = TreeNode(arr[0])
    for i in range(1, len(arr)):
        insert_node(root, arr[i])
    
    return root

def insert_node(root, key):
    if not root:
        return TreeNode(key)
    
    queue = [root]
    while queue:
        node = queue.pop(0)
        if not node.left:
            node.left = TreeNode(key)
            break
        else:
            queue.append(node.left)
        
        if not node.right:
            node.right = TreeNode(key)
            break
        else:
            queue.append(node.right)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)

# Example usage:
elements = [1, 2, 3, 4, 5, 6, 7]
root = insert_into_tree(elements)
print("Inorder traversal of the constructed tree:")
inorder_traversal(root)



class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_into_tree(arr):
    if not arr:
        return None
    
    root = TreeNode(arr[0])
    stack = [(root, 0)]  # Stack to keep track of nodes and their corresponding index in the array
    
    for i in range(1, len(arr)):
        node, parent_idx = stack[-1]  # Get the top node and its parent index from the stack
        
        # Determine whether to insert the current element as left or right child
        if parent_idx % 2 == 0:  # If the parent's index is even, insert as left child
            node.left = TreeNode(arr[i])
            stack.append((node.left, i))  # Push the left child and its index to the stack
        else:  # If the parent's index is odd, insert as right child
            node.right = TreeNode(arr[i])
            stack.append((node.right, i))  # Push the right child and its index to the stack
        
        # Backtrack to the parent node if the current node has both left and right children
        while len(stack) > 1 and (stack[-1][1] - stack[-2][1] == 1):
            stack.pop()
    
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

# Example usage:
elements = [1, 2, 3, 4, 5, 6, 7]
root = insert_into_tree(elements)
print("Inorder traversal of the constructed tree:")
inorder_traversal(root)
