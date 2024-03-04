#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.hd = 0  

def top_view(root):
    if not root:
        return

    top_view_dict = {}

    queue = []
    queue.append(root)

    while queue:
        temp_node = queue.pop(0)
        hd = temp_node.hd

        if hd not in top_view_dict:
            top_view_dict[hd] = temp_node.data

        if temp_node.left:
            temp_node.left.hd = hd - 1
            queue.append(temp_node.left)

        if temp_node.right:
            temp_node.right.hd = hd + 1
            queue.append(temp_node.right)

    for key in sorted(top_view_dict):
        print(top_view_dict[key], end=" ")

root = Node(9)
root.left = Node(7)
root.right = Node(1)
root.left.right = Node(4)
root.left.left = Node(6)
root.left.left.right = Node(5)
root.right.left = Node(3)
root.right.left.left = Node(11)
root.right.right = Node(2)
root.right.left.right = Node(12)
root.right.left.right.right = Node(17)

print("Top View of Binary Tree:")
top_view(root)


# In[ ]:




