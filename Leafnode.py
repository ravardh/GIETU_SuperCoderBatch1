class node:
    def __init__(self,info=None):
        self.data = info
        self.left = None
        self.right = None
        self.key = None

def leafnode(root):
    if root == None:
        return
    leafnode(root.left) 
    leafnode(root.right)
    if root.right == None and root.left == None:
        print(root.data, end=" ")


# First tree
# root = node(20)

# root.left = node(32)
# root.right = node(10)

# root.left.left = node(15)
# root.left.right = node(12)
# root.right.left = node(8)
# root.right.right = node(24)

# root.left.left.left = node(4)
# root.left.right.left = node(50)
# root.left.right.right = node(6)
# root.right.right.left = node(16)
# root.right.right.right = node(2)

# root.left.right.left.left = node(40)
# root.left.right.left.right = node(35)
        

#Second Tree
# root=node(20)
# root.left=node(10)
# root.right=node(12)

# root.left.left=node(30)
# root.left.right=node(45)
# root.left.left.left=node(4)
# root.left.left.right=node(5)


# Thrid tree
root = node(9)

root.left=node(7)
root.right=node(1)

root.left.left=node(6)
root.left.right=node(4)
root.right.left=node(3)
root.right.right=node(2)

root.left.right.left = node(4)
root.left.right.right = node(6)
root.right.right.left = node(16)
root.right.right.right = node(2)

leafnode(root)
