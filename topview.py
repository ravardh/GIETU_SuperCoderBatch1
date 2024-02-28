class node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        self.key = 0

def topView(root):
    Q = [root]
    key = 0
    root.key = key
    tv = {}

    while len(Q) > 0:
        current = Q.pop(0)
        key = current.key
        if current != None:
            if key not in tv:
                tv[key] = current.data

            if current.left != None:
                Q.append(current.left)
                current.left.key = key - 1
            if current.right != None:
                Q.append(current.right)
                current.right.key = key + 1
    
    for x in sorted(tv.keys()):
        print(tv[x], end = " ")

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
root.left.right.left.left = node(48)
root.left.right.left.right = node(35)

print(topView(root))

def findHeight(root):
    if root == None: return 0

    right_height = findHeight(root.right)
    left_height = findHeight(root.left)

    return max(right_height, left_height) + 1

def leafNode(root):
    if root == None: return 0

    if root.left == None and root.right == None: return root.data

    return 0