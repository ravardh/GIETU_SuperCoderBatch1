#Left view 
class Node:
    def _init_(self, key):
        self.data = key
        self.left = None
        self.right = None

def leftViewRec(root, level, ml):
    if root is None:
        return

    if (ml[0] < level):
        print(root.data)
        ml[0] = level

    leftViewRec(root.left, level+1, ml)
    leftViewRec(root.right, level+1, ml)

def leftView(root):
    ml = [0]
    leftViewRec(root, 1, ml)

root = Node(9)

root.left = Node(7)
root.right = Node(1)

root.left.left = Node(6)
root.left.right = Node(4)
root.right.left = Node(3)
root.right.right = Node(2)

root.left.left.right = Node(5)
root.right.left.left = Node(11)
root.right.left.right = Node(12)

root.right.left.right.right = Node(17)

leftView(root)
