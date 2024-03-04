class node(object):
    def __init__(self,info=None):
        self.data = info
        self.left=None
        self.right=None

def preorder(root):
    if root is None:
        return
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=' ')

def levelorder(root):
    Q=[root]
    Q.append(None)
    while len(Q)>0:
        cur = Q.pop(0)
        if(cur==None):
            print()
            if len(Q)>0:
                 Q.append(None)
        else:
            print(cur.data,end=' ')
            if cur.left != None:
                Q.append(cur.left)
            if cur.right !=None:
                Q.append(cur.right) 

root=node(20)
root.left=node(32)
root.right=node(10)
root.left.left=node(15)
root.left.right=node(12)
root.right.left=node(8)
root.right.right=node(24)
root.left.left.left=node(4)
root.left.right.left=node(50) 
root.right.right.left=node(16)       
root.right.right.right=node(2)
root.left.right.left.left=node(40)
root.left.right.left.right=node(35)

print("Preorder traversal:")
preorder(root)
print("\nInorder traversal:")
inorder(root)
print("\nPostorder traversal:")
postorder(root)
print("\nlevelorder traversal:")
levelorder(root)