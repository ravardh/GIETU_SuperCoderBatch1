class Node:
 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
 
def leftViewUtil(root, level, curlevel):
 
    if root is None:
        return
 
    if (curlevel[0] < level):
        print (root.data, end = " ")
        curlevel[0] = level
 
    leftViewUtil(root.left, level + 1, curlevel)
    leftViewUtil(root.right, level + 1, curlevel)
 
 
def leftView(root):
    curlevel = [0]
    leftViewUtil(root, 1, curlevel)
 
 
if __name__ == '__main__':
    root = Node(9)
    root.left = Node(7)
    root.right = Node(1)
    root.left.left = Node(6)
    root.left.right = Node(4)
    root.left.left.right = Node(5)
    root.right.right = Node(2)
    root.right.left = Node(3)
    root.right.left.left = Node(10)
    root.right.left.right = Node(12)
    root.right.left.right.right = Node(17)

     
    leftView(root)
    
    
#  Right view


class Node:
 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
 
def rightViewUtil(root, level, curlevel):
 
    if root is None:
        return
 
    if (curlevel[0] < level):
        print (root.data, end = " ")
        curlevel[0] = level
 
    rightViewUtil(root.right, level + 1, curlevel)
    rightViewUtil(root.left, level + 1, curlevel)
 
 
def rightView(root):
    curlevel = [0]
    rightViewUtil(root, 1, curlevel)
 
 
if __name__ == '__main__':
    root = Node(9)
    root.left = Node(7)
    root.right = Node(1)
    root.left.left = Node(6)
    root.left.right = Node(4)
    root.left.left.right = Node(5)
    root.right.right = Node(2)
    root.right.left = Node(3)
    root.right.left.left = Node(10)
    root.right.left.right = Node(12)
    root.right.left.right.right = Node(17)

     
    rightView(root)