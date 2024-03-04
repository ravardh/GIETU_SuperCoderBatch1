class node:
    def __init__(self,value=None):
        self.data = value
        self.left = None
        self.right = None
        self.height = 0

class AVLTree(object):
    def insert(self,root,value):
        if root == None:
           return node(value)
        if value < root.data:
            root.left = self.insert(root.left,value)
        if value > root.data:
            root.right = self.insert(root.right,value)
        
        root.height = 1 + max(self.ght(root.left),self.ght(root.right))

        BF = self.bal(root)

        if BF > 1 and value < root.left.data:
            return self.LRotate(root)
        
        elif BF > -1 and value > root.right.data:
            return self.RRotate(root)
        
        elif BF > 1 and value > root.left.data:
            root.left = self.RRotate(root.left)
            return self.LRotate(root)
        
        elif BF < -1 and value < root.right.data:
            root.right = self.LRotate(root.right)
            return self.RRotate(root)
        
        return root
    def ght(self,root):
        if root == None:
            return 0
        return root.height
    def bal(self,root):
        if root == None:
            return 0
        return self.ght(root.left)-self.ght(root.right)
    def LRotate(self,root):
        B = A.left
        temp = B.right

        B.right = A
        A.left = temp

        A.height = 1 + max(self.ght(root.left),self.ght(root.right))
        B.height = 1 + max(self.ght(root.left),self.ght(root.right))

        return B
    def preorder(self,root):
        if root == None:
            return
        print(root.data, end= " ")
        self.preorder(root.left) 
        self.preorder(root.right)

tree = AVLTree()
value_list = [50,45,55,35,40,48,60,20,70,41,47,42,15,22,25,30,90]
root = None
for x in value_list:
    root = tree.insert(root.X)
tree.preorder(root)
