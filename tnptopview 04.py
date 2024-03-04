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
def leftView(root):
    if not root:
        return
    queue = [root]
    while queue:
        n = len(queue)
        for i in range(n):
            temp = queue.pop(0)
            if i == 0:
                print(temp.data, end=" ")
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

def rightView(root):
    if not root:
        return
    queue = [root]
    while queue:
        n = len(queue)
        for i in range(n):
            temp = queue.pop(0)
            if i == n - 1:
                print(temp.data, end=" ")
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)


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

print("\n\nTop View")
topView(root)

print("\n\nLeft View:")
leftView(root)

print("\n\nRight View:")
rightView(root)