class node:
    def _init_(self,info=None):
        self.data=info
        self.left=None
        self.right=None
        self.key=0

def topview(root):
    Q=[root]
    key=0
    root.key=key
    TV=dict()
    while len(Q)>0 :
        curr =Q.pop(0)
        key=curr.key
        if curr != None:
            if key not in TV:
                TV[key]=curr.data
            if curr.left != None:
                Q.append(curr.left)
                curr.left.key=key-1
            if curr.right != None:
                Q.append(curr.right)
                curr.right.key=key+1
    for x in sorted(TV.keys()):
        print(TV[x],end=" ")
    
        

root = node(2)

root.left = node(10)
root.right = node(82)

root.left.left = node(12)
root.left.right = node(4)

root.right.left = node(9)
root.right.right = node(6)
root.right.right.left = node(84)
root.right.right.right = node(1)
root.right.right.right.left = node(16)
root.right.right.right.right = node(5)

root.left.right.left = node(32)
root.left.right.right = node(92)
root.left.right.left.left = node(42)
root.left.right.left.right = node(7)

root.left.right.left.left.left = node(46)
root.left.right.left.left.left.left = node(17)



topview(root)