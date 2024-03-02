class node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):

    def insert(self, root, value):
        if root is None:
            return node(value)

        if value < root.data:
            root.left = self.insert(root.left, value)
        elif value > root.data:
            root.right = self.insert(root.right, value)
        
        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance(root)

        if balance > 1 and value < root.left.data:
            return self.rightrotate(root)

        if balance < -1 and value > root.right.data:
            return self.leftrotate(root)

        if balance > 1 and value > root.left.data:
            root.left = self.leftrotate(root.left)
            return self.rightrotate(root)

        if balance < -1 and value < root.right.data:
            root.right = self.rightrotate(root.right)
            return self.leftrotate(root)

        return root

    def height(self, root):
        if root is None:
            return 0
        return root.height

    def balance(self, root):
        if root is None:
            return 0
        return self.height(root.left) - self.height(root.right)

    def leftrotate(self, A):
        B = A.right
        T = B.left

        B.left = A
        A.right = T

        A.height = 1 + max(self.height(A.left), self.height(A.right))
        B.height = 1 + max(self.height(B.left), self.height(B.right))

        return B

    def rightrotate(self, A):
        B = A.left
        T = B.right

        B.right = A
        A.left = T

        A.height = 1 + max(self.height(A.left), self.height(A.right))
        B.height = 1 + max(self.height(B.left), self.height(B.right))

        return B

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)
    

tree = AVLTree()

root = None
V_L = [50, 36, 12, 20, 76, 18, 44, 52, 90]
for x in V_L:
    root = tree.insert(root, x)

print(root.data)  # Output: 36
tree.inorder(root)  # Output: 12 18 20 36 44 50 52 76 90
