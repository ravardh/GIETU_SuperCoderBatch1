class node:
    def __init__(self,info=None):
        self.data = info
        self.left=None
        self.right=None

def preorder(root):
    if root==None:
        return
    print(root.data,end=' ')
    preorder(root.left)
    preorder(root.right)

root=node(20)
root.left=node(32)
root.right=node(10)
root.left.left=node(15)
root.left.right=node(12)
root.right.left=node(8)
root.right.right=node(24)
root.left.left.left=node(4)
root.left.right.left=node(50) 
root.right.right.left=node(16)       
root.right.right.right=node(2)
root.left.right.left.left=node(40)
root.left.right.left.right=node(35)

print(root)
print(root.data)
preorder(root)