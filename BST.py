class node:
    def __init__(self,info=None):
        self.data = info
        self.left = None
        self.right = None

def bst(root,ele):
    if root == None:
        return node(ele)
    if (ele >= root.data):
        root.right = bst(root.right,ele)
    else:
        root.left = bst(root.left,ele)
    return root
    




# Thrid tree
root = node(9)

root.left=node(7)
root.right=node(1)

root.left.left=node(6)
root.left.right=node(4)
root.right.left=node(3)
root.right.right=node(2)
# bst(arr)

# arr = [10,14,17,9,5,15,12,7,8,2,3]