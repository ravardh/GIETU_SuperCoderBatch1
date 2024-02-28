class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def rightViewRec(root, level, ml):
    if root is None:
        return

    if (ml[0] < level):
        print(root.data)
        ml[0] = level

    rightViewRec(root.right, level + 1, ml)
    rightViewRec(root.left, level + 1, ml)

def rightView(root):
    ml = [0]
    rightViewRec(root, 1, ml)

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

rightView(root)
