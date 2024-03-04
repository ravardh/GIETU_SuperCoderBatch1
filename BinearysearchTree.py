#Binary search tree
class node:
    def __init__(self, info=None):
        self.data = info
        self.left = None
        self.right = None


def construct_BST(arr):
    if not arr:
        return None

    mid = len(arr) // 2
    root = node(arr[mid])

    root.left = construct_BST(arr[:mid])
    root.right = construct_BST(arr[mid + 1:])

    return root

def levelorder(root):
    Q = [root]
    Q.append(None)
    while len(Q) > 0:
        cur = Q.pop(0)
        if cur is None:
            print()
            if len(Q) > 0:
                Q.append(None)
        else:
            print(cur.data, end=" ")
            if cur.left is not None:
                Q.append(cur.left)
            if cur.right is not None:
                Q.append(cur.right)
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
root = construct_BST(arr)

levelorder(root)