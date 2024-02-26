class node:
    def __init__(self,info=None):
        self.data=info
        self.left=None
        self.right=None
def preorder(root):
    if(root==None):
        return
    print(root.data,end=' ')
    preorder(root.left)
    preorder(root.right)
def postorder(root):
    if(root==None):
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=' ')
def inorder(root):
    if(root==None):
        return
    inorder(root.left)
    print(root.data,end=' ')
    inorder(root.right)
def levelorder(root):
    Q=[root]
    Q.append(None)
    while len(Q)>0:
        cur=Q.pop(0)
        if cur==None:
            print()
            if(len(Q)>0):
              Q.append(None)
        else:
            print(cur.data,end=' ')
            if cur.left !=None:
                Q.append(cur.left)
            if cur.right!=None:
                Q.append(cur.right)
root=node(20)
node2=node(32)
node3=node(10)
node4=node(15)
node5=node(12)
node6=node(8)
node7=node(24)
node8=node(11)
node9=node(50)
node10=node(6)
node11=node(16)
node12=node(2)
node13=node(48)
node14=node(35)
root.left=node2
root.right=node3
node2.left=node4
node2.right=node5
node3.left=node6
node3.right=node7
node4.left=node8
node5.left=node9
node5.right=node10
node7.left=node11
node7.right=node12
node9.left=node13
node9.right=node14
print("\nPre Order:\n")
preorder(root)
postorder(root)
inorder(root)
print("\nLevel Order:\n")
levelorder(root)