class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
      
def findHeight(root):
    if(root==None):
        return 0
    leftHeight=findHeight(root.left)
    rightHeight=findHeight(root.right)
    return max(leftHeight,rightHeight)+1

def leafNode(root):
    if root == None :
        return
    if root.left==None and root.right==None :
        print(root.data,end=" ")
    leafNode(root.left)
    leafNode(root.right)

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(4)
root.left.right.right=TreeNode(5)
root.left.right.right.right=TreeNode(6)

height=findHeight(root)
print("Height of the tree:",height)

print("The Leaf Nodes are")
leafNode(root)