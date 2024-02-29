class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.key=0
        
def topView(root):
    q=[root]
    key=0
    root.key=key
    tv=dict()
    while len(q)>0:
        cur=q.pop(0)
        key=cur.key
        if key not in tv:
            tv[key]=cur.data
        if cur.left:
            q.append(cur.left)
            cur.left.key=key-1
        if cur.right:
            q.append(cur.right)
            cur.right.key=key+1
    for x in sorted(tv):
        print(tv[x],end=" ")
        
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(4)
root.left.right.right=TreeNode(5)
root.left.right.right.right=TreeNode(6)

print("The top view of the tree is: ")
topView(root)
