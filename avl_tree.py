class node:
    def init(self,value):
        self.data = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):

    def insert(self,root,value):
        if root == None:
            return node(value)
        if(value<root.data):
            root.left = self.insert(root.left,value)
        elif value>root.data:
            root.right = self.insert(root.right,value)
        
        root.height = 1 + max(self.ght(root.left),
                              self.ght(root.right))


        bl = self.bal(root)

        if bl > 1 and value < root.left.data:
            return self.leftrotate(root)

        if bl > 1 and value > root.left.data:
            root.left = self.rightrotate(root.left)
            return self.leftrotate(root)

        if bl < -1 and value > root.right.data:
            return self.rightrotate(root)

        if bl < -1 and value < root.right.data:
            root.right = self.leftrotate(root.right)
            return self.rightrotate(root)
        return root

    def ght(self,root):
        if root == None:
            return 0
        return root.height

    def bal(self,root):
        if root == None:
            return 0
        return self.ght(root.left)-self.ght(root.right)

    def leftrotate(self,A):
        B = A.left
        temp = B.right
        B.right = A
        A.left = temp

        A.height = 1 + max(self.ght(root.left),
                              self.ght(root.right))
        B.height = 1 + max(self.ght(root.left),
                              self.ght(root.right))
        return B

    def rightrotate(self,A):
        B = A.right
        temp = B.left
        B.left = A
        A.right = temp

        A.height = 1 + max(self.ght(root.left),
                              self.ght(root.right))
        B.height = 1 + max(self.ght(root.left),
                              self.ght(root.right))
        return B

    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)
    

tree = AVLTree()

root = None
V_L = [50 , 36, 12, 20, 76, 18, 44, 52, 90]
for x in V_L:
    root = tree.insert(root,x)

print(root)

tree.inorder(root)
