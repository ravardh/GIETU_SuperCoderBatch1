class node:
    def __init__(self,data = None):
        self.dataval = data
        self.left = None
        self.right = None

def preorder(root):#root left right
    if root == None:
        return
    print(root.dataval,end = ' ')
    preorder(root.left)
    preorder(root.right)

def postorder(root):#left right root
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.dataval,end = ' ')

def levelorder(root):#level wise printing
    Q = [root]
    Q.append(None)

    while len(Q) > 0:
        current = Q.pop(0)
        if current == None:
            print()
            if len(Q) > 0:
                Q.append(None)
        else:
            print(current.dataval, end=' ')
            if current.left != None:
                Q.append(current.left)
            if current.right != None:
                Q.append(current.right)
                    
root = node(20)

root.left = node(32)
root.right = node(10)

root.left.left = node(15)
root.left.right = node(12)
root.right.left = node(8)
root.right.right = node(24)

root.left.left.left = node(4)
root.left.right.left = node(50)
root.left.right.right = node(6)
root.right.right.left = node(16)
root.right.right.right = node(2)

root.left.right.left.left = node(40)
root.left.right.left.right = node(35)

print('The preorder traversal is ')
preorder(root)
print()
print('The postorder traversal is ')
postorder(root)
print()
print('The level order traversal is ')
levelorder(root)
