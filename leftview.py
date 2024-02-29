class node:
    def __init__(self,info=None):
        self.data = info
        self.left = None
        self.right = None
        self.key = 0

def leftview(root):
    if not root:
        return
    
    Q=[root]
    while Q:
        size = len(Q)
        for i in range(size):
            node = Q.pop(0)
                
            if i == 0:
                print(node.data,end=" ")
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)
    print()
    
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

print(root)
print(root.data)

print("\n\nLeftview is")
leftview(root)