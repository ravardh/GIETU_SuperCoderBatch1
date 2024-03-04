class node:
    def __init__(self, info=None):
        self.data = info
        self.left = None
        self.right = None

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

root.left.right.left.left = node(40)
root.left.right.left.right = node(35)

print(root.left.data)

def preOrder(root):
    if root==None:
        return
    print(root.data, end=" ")
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):
    if root==None:
        return
    inOrder(root.left)
    print(root.data, end=" ")
    inOrder(root.right)

def postOrder(root):
    if root==None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end=" ")
    
def levelOrder(root):
    Q = [root]
    while len(Q)>0:
        cur = Q.pop(0)
        if cur==None:
            continue
        print(cur.data, end=" ")
        Q.append(cur.left)
        Q.append(cur.right)

print("PreOrder traversal")
preOrder(root)
print("\nInOrder traversal")
inOrder(root)
print("\nPostOrder traversal")
postOrder(root)
print("\nLevelOrder traversal")
levelOrder(root)
