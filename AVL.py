class Node:
    def _init_(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def get_height(node):
    if not node:
        return 0
    return node.height


def get_balance_factor(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = max(get_height(y.left), get_height(y.right)) + 1
    x.height = max(get_height(x.left), get_height(x.right)) + 1

    return x


def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = max(get_height(x.left), get_height(x.right)) + 1
    y.height = max(get_height(y.left), get_height(y.right)) + 1

    return y


def insert(root, key):
    if not root:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance_factor(root)

    
    if balance > 1 and key < root.left.key:
        return rotate_right(root)

    
    if balance < -1 and key > root.right.key:
        return rotate_left(root)

    
    if balance > 1 and key > root.left.key:
        root.left = rotate_left(root.left)
        return rotate_right(root)

    # Right-Left case
    if balance < -1 and key < root.right.key:
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root


def construct_avl_tree(arr):
    root = None
    for key in arr:
        root = insert(root, key)
    return root


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=' ')
        inorder_traversal(root.right)
        
def levelorder(root):
    queue=[]
    queue.append(root)
    queue.append(None)
    while len(queue)>1:
        front=queue.pop(0)
        if front is not None:
            print(front.key,end=" ")
            if front.left!=None:
                queue.append(front.left)
            if front.right!=None:
                queue.append(front.right)
        else:
            print()
            queue.append(None)
            
array = [50,45,55,35,40,48,60,20,70,41,47,42,15,22,25,30,90]
avl_root = construct_avl_tree(array)



print("Levelorder Traversal of AVL Tree:")
levelorder(avl_root)