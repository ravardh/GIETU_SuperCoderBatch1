#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Right view
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def levelorder(root):
    Q = [root]
    Q.append(None)
    while len(Q) > 0:
        cur = Q.pop(0)
        if cur == None:
            print()
            if len(Q) > 0:
                Q.append(None)
        else:
            print(cur.info, end=' ')
            if cur.left != None:
                Q.append(cur.left)
            if cur.right != None:
                Q.append(cur.right)

def right_view(root):
    result = []

    def dfs(node, level):
        nonlocal result
        if node is None:
            return
        if level == len(result):
            result.append(node.info)
        # Traverse right child first for the right view
        dfs(node.right, level + 1)
        dfs(node.left, level + 1)

    dfs(root, 0)
    return result

root = Node(20)
root.left = Node(32)
root.right = Node(10)
# level2
root.left.left = Node(15)
root.left.right = Node(12)
root.right.left = Node(8)
root.right.right = Node(24)
# level3
root.left.left.left = Node(4)
root.left.right.left = Node(50)
root.left.right.right = Node(6)
root.right.right.left = Node(16)
root.right.right.right = Node(16)
root.left.right.left.left = Node(40)
root.left.right.left.right = Node(35)

levelorder(root)
print("Right view:", right_view(root))


# In[ ]:




