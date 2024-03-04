#data= 10,14,17,9,5,15,12,7,8,2,3
class node:
    def __init__(self,info=None):
        self.data=info
        self.left=None
        self.right=None
def insertion(root,ele):
    if(root==None):
        root=node(ele)
        return
    elif(ele>root.data):
        if(root.right==None):
            root.right=node(ele)
            return
        insertion(root.right,ele)

    elif (ele<root.data):
        if(root.left==None):
            root.left=node(ele)
            return
        insertion(root.left,ele)   
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
    
lst=[10,14,17,9,5,15,12,7,8,2,3]
root=node(lst[0])
for i in range(1,len(lst)):
    insertion(root,lst[i])
print("Inorder Traversal:\n")
inorder(root)

