class node:
    def __init__(self,info=None):
        self.data = info
        self.left = None
        self.right = None
        



def topview(root):
    if root is None:
        return

    # Dictionary to store the horizontal distance of nodes from the root
    hd_dict = {}
    # Queue for level order traversal
    Q = [(root, 0)]

    # Level order traversal
    while Q:
        cur, hd = Q.pop(0)

        # If hd is not in the dictionary, add the node to the dictionary
        if hd not in hd_dict:
            hd_dict[hd] = cur.data

        # Enqueue left child with hd - 1 and right child with hd + 1
        if cur.left:
            Q.append((cur.left, hd - 1))
        if cur.right:
            Q.append((cur.right, hd + 1))

    # Print nodes from the dictionary sorted by their horizontal distance
    for key in sorted(hd_dict):
        print(hd_dict[key], end=" ")



# First tree
# root = node(20)

# root.left = node(32)
# root.right = node(10)

# root.left.left = node(15)
# root.left.right = node(12)
# root.right.left = node(8)
# root.right.right = node(24)

# root.left.left.left = node(4)
# root.left.right.left = node(50)
# root.left.right.right = node(6)
# root.right.right.left = node(16)
# root.right.right.right = node(2)

# root.left.right.left.left = node(40)
# root.left.right.left.right = node(35)
        

#Second Tree
# root=node(20)
# root.left=node(10)
# root.right=node(12)

# root.left.left=node(30)
# root.left.right=node(45)
# root.left.left.left=node(4)
# root.left.left.right=node(5)


# Thrid tree
root = node(9)

root.left=node(7)
root.right=node(1)

root.left.left=node(6)
root.left.right=node(4)
root.right.left=node(3)
root.right.right=node(2)

# root.left.left.left = node(4)
# root.left.right.left = node(4)
# root.left.right.right = node(6)
# root.right.right.left = node(16)
# root.right.right.right = node(2)


topview(root)