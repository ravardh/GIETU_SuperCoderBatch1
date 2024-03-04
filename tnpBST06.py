class Node:
    def __init__(self, ele):
        self.left = self.right = None
        self.val = ele

def insert(root, ele):
    if root is None:
        return Node(ele)
    if ele < root.val:
        root.left = insert(root.left, ele)
    else:
        root.right = insert(root.right, ele)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

lst = [10,14,17,9,5,15,12,7,8,2,3]
root = None

for ele in lst:
    root = insert(root, ele)

inorder(root)