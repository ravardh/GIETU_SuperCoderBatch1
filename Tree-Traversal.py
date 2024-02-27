class node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

def preOrderTraversal(root):
    if root == None: return
    print(root.data, end = " ")
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)

def postOrderTraversal(root):
    if root == None: return
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.data, end = " ")

def inOrderTraversal(root):
    if root == None: return
    inOrderTraversal(root.left)
    print(root.data, end = " ")
    inOrderTraversal(root.right)

def levelOrderTraversal(root):
    Q = [root]
    Q.append(None)

    while len(Q) > 0:
        current = Q.pop(0)
        if current == None:
            print()
            if len(Q) > 0: Q.append(None)
        else:
            print(current.data, end = " ")
            if current.left != None:
                Q.append(current.left)
            if current.right != None:
                Q.append(current.right)



root = node(20)

root.left = node(32)
root.right = node(10)

root.left.left = node(15)
root.left.right = node(12)
root.right.left = node(8)
root.right.right = node(24)

root.left.left.left = node(4)
root.left.right.left = node(50)
root.left.right.right = node(6)
root.right.right.left = node(16)
root.right.right.right = node(2)

root.left.right.left.left = node(48)
root.left.right.left.right = node(35)

print("Pre-Order Traversal:")
preOrderTraversal(root)
print("\n\nPost-Order Traversal:")
postOrderTraversal(root)
print("\n\nIn-Order Traversal:")
inOrderTraversal(root)
print("\n\nLevel-Order Traversal:")
levelOrderTraversal(root)