class TreeNode:
    def __init__(self, key):
        self.key = key
        self.l = None
        self.r = None

def new_key_insert(root, new_key):
    if root is None:
        root = TreeNode(new_key)
        return root
    if new_key < root.key:
        root.l = new_key_insert(root.l, new_key)
    else:
        root.r = new_key_insert(root.r, new_key)
    return root

def display(root):
    if root:
        display(root.l)
        print(root.key)
        display(root.r)


r = TreeNode(50)
r = new_key_insert(r, 30)
r = new_key_insert(r, 20)
r = new_key_insert(r, 40)
r = new_key_insert(r, 70)
r = new_key_insert(r, 60)
r = new_key_insert(r, 80)

display(r)

