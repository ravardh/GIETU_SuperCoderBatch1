class Node:
    def __init__(self,info):
        self.data=info
        self.left=None
        self.right=None
root=Node(20)
root.left=Node(32)
root.right=Node(10)
root.left.left=Node(15)
root.left.right=Node(12)
root.right.left=Node(8)
root.right.right=Node(24)
root.left.left.left=Node(4)
root.left.right.left=Node(50)
root.left.right.right=Node(6)
root.left.right.left.left=Node(40)
root.left.right.left.right=Node(35)
root.right.right.left=Node(16)
root.right.right.right=Node(2)
def inorder(root):
    if(root==None):
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
inorder(root)
