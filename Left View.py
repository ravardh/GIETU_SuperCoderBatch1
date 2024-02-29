class node:
    def __init__(self,data = None):
        self.dataval = data
        self.left = None
        self.right = None

def leftview(root):#level wise printing
    Q = [root]
    Q.append(None)
    print(root.dataval,end = ' ')
    
    while len(Q) > 0:
        current = Q.pop(0)
        if current == None and Q[0] != None:
            print(Q[0].dataval, end=' ')
            if len(Q) > 0:
                Q.append(None)
        else:
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
                    
root = node(9)

root.left = node(7)
root.right = node(1)

root.left.left = node(6)
root.left.right = node(4)
root.right.left = node(3)
root.right.right = node(2)

root.left.left.right = node(5)

root.right.left.left = node(11)
root.right.left.right = node(12)

root.right.left.right.right = node(17)

print('The left view of a tree is ')
leftview(root)
print('The leaf nodes are')
findLeafNode(root)
