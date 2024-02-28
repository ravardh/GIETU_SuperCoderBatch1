#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Node:
 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
 
def maxDepth(node):
    if node is None:
        return 0
 
    else:
 
        
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
 

        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1
 

root = Node(1)
root.left = Node(5)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(17)
root.left.left.left = Node(20)
root.left.right.left = Node(11)
root.left.right.right = Node(3)
root.right.right.left = Node(12)
root.right.right.right = Node(16)
root.left.left.left.right = Node(10)
root.right.right.left.left = Node(14)
root.right.right.left.right = Node(19)
root.left.left.left.right.left = Node(21)
root.right.right.left.right.right = Node(18)
root.left.left.left.right.left.left = Node(13)
root.right.right.left.right.right.right = Node(15)



 
 
print("Height of tree is %d" % (maxDepth(root)))


# In[ ]:




