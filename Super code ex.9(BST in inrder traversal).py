#create a BST in inreder traversal:
class Node:
    def __init__(self,info=None):
        self.data=info
        self.left=None
        self.right=None
def insertion(root,ele):
    if(root==None):
        root=Node(ele)
        return
    elif(ele>root.data):
        if(root.right==None):
            root.right=Node(ele)
            return
        insertion(root.right,ele)

    elif (ele<root.data):
        if(root.left==None):
            root.left=Node(ele)
            return
        insertion(root.left,ele) 
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
