class node:
    def __init__(self,data = None):
        self.dataval = data
        self.left = None
        self.right = None

def rightview(root):#level wise printing
    Q = [root]
    Q.append(None)

    while len(Q) > 0:
        current = Q.pop(0)
        if current == None:
            if len(Q) > 0:
                Q.append(None)
        else:
            if current != None and Q[0] == None:
                print(current.dataval, end=' ')
            if current.left != None:
                Q.append(current.left)
            if current.right != None:
                Q.append(current.right)

def findLeafNode(root):#root left right
    i = 0
    if root == None:
        return
    if root.right == None and root.left == None:
        print(root.dataval, end = ' ')
    findLeafNode(root.left)
    findLeafNode(root.right)
                    
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

print('The right view is ')
rightview(root)
print()
print('The leaf nodes are')
findLeafNode(root)
