class node:
    def __init__(self, info=None):
        self.data=info
        self.left=None
        self.right=None

def leafnode(root):
    if(root == None):
        return
    if(root.left == None and root.right == None):
        print(root.data, end = " ")
    leafnode(root.left)
    leafnode(root.right)


root = node(2)

root.left = node(10)
root.right = node(82)

root.left.left = node(12)
root.left.right = node(4)
root.right.left = node(9)
root.right.right = node(6)

root.left.right.left = node(32)
root.left.right.right = node(92)
root.right.right.left = node(84)
root.right.right.right = node(1)

root.left.right.left.left = node(42)
root.left.right.left.right = node(7)
root.right.right.right.left = node(16)
root.right.right.right.right = node(5)

root.left.right.left.left.left = node(46)
root.left.right.left.left.left = node(17)

leafnode(root)
