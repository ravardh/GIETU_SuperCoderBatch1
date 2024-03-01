#create a BST in inreder traversal:
class Node:
    def __init__(self,info=None):
        self.data=info
        self.left=None
        self.right=None
def insertion(root,ele):
    if root == None:
        return Node(ele)
    if(ele>=root.data):
        root.right = insertion(root.right,ele)
    else:
        root.left = insertion(root.left,ele)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)
lst = [12,23,5,7,9,3,4,16,14,10,2,0]
root=Node(lst[0])
for i in range(1,len(lst)):
    insertion(root,lst[i])
print("Inorder Traversal:\n")
inorder(root)
