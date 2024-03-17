class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.key=0
        
def leftView(root):
    q=[]
    q.append(root)
    q.append(None)
    print(root.data)
    while len(q)>1:
        curr=q.pop(0)
        if(curr!=None):
            if(curr.left):
                q.append(curr.left)
            if(curr.right):
                q.append(curr.right)
        if(curr==None):
           print(q[0].data)
           q.append(None)
           
root=TreeNode(9)
root.left=TreeNode(7)
root.right=TreeNode(1)
root.left.left=TreeNode(6)
root.left.right=TreeNode(4)
root.right.left=TreeNode(3)
root.right.right=TreeNode(2)
root.left.left.right=TreeNode(5)
root.right.left.left=TreeNode(10)
root.right.left.right=TreeNode(12)
root.right.left.right.right=TreeNode(17)

print("The left view of the tree is: ")
leftView(root)