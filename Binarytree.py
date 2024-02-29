class node:
    def _init_(self, key):
        self.left = None
        self.right = None
        self.data = key


def insert(root, key):
    if root is None:
        return node(key)
    else:
        if root.data < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
    
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)
        
def binarySearchTree(arr):
    r = node(arr[0])
    for i in arr[1:]:
        r = insert(r, i)
    return r
    
arr = [10, 14, 17, 9, 5, 15, 12, 7, 8, 2, 3]
root = binarySearchTree(arr)
inOrder(root)