# I've noticed a couple of issues in your code. The main one is that you are creating the tree with incorrect connections. Also, there is a typo in the function `preorder` where it prints the data of the root node. I've corrected these issues in the code below:


class node:
    def __init__(self, info=None):
        self.data = info
        self.left = None
        self.right = None

def preorder(root):  # root, left, right
    if root is None:  # Base Case
        return
    print(root.data, end=" ")  # Executable statement to print Root data
    preorder(root.left)  # recursive call for left child
    preorder(root.right)  # recursive call for right child

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")

def levelorder(root):
    if root is None:
        return
    Q = [root]
    while Q:
        cur = Q.pop(0)
        print(cur.data, end=" ")
        if cur.left is not None:
            Q.append(cur.left)
        if cur.right is not None:
            Q.append(cur.right)

# Corrected tree construction
root = node(20)

root.left = node(32)
root.right = node(10)

root.left.left = node(15)
root.left.right = node(12)
root.right.left = node(8)
root.right.right = node(24)

root.left.right.left = node(40)
root.left.right.right = node(35)

print(root)
print(root.data)


print("\nPreorder Traversal")
preorder(root)
print("\n\nInorder Traversal")
inorder(root)
print("\n\nPostorder Traversal")
postorder(root)
print("\n\nLevelorder Traversal")
levelorder(root)


# In this corrected code, I fixed the tree construction to ensure correct connections between nodes, and I corrected the `preorder` function's print statement.