arr = [10, 14, 17, 9, 5, 15, 12, 7, 8, 2, 3]

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bst_insert(root, data):
    if root is None:
        return TreeNode(data)

    if data < root.data:
        root.left = bst_insert(root.left, data)
        
    elif data > root.data:
        root.right = bst_insert(root.right, data)

    return root

def construct_bst(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    for i in range(1, len(arr)):
        root = bst_insert(root, arr[i])

    return root

def levelorder(root):
    queue=[]
    queue.append(root)
    queue.append(None)
    while len(queue)>1:
        front=queue.pop(0)
        if front is not None:
            print(front.data,end=" ")
            if front.left!=None:
                queue.append(front.left)
            if front.right!=None:
                queue.append(front.right)
        else:
            print()
            queue.append(None)
            
root = construct_bst(arr)
levelorder(root)