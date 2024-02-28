class node:
    def __init__(self, info=None):
        self.data=info
        self.left=None
        self.right=None
        self.key = 0
        
def topview(root):
    Q = [root]
    key = 0
    root.key = key
    TV = dict()
    while len(Q)>0:
        cur = Q.pop(0)
        key = cur.key
        if cur != None:
            if key not in TV:
                TV[key] = cur.data
            if cur.left != None:
                Q.append(cur.left)
                cur.left.key = key-1
            if cur.right != None:
                Q.append(cur.right)
                cur.right.key = key+1
    for x in sorted(TV.keys()):
        print(TV[x],end=" ")

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

topview(root)
