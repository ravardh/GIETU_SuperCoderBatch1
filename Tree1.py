# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 10:18:47 2024

@author: HP
"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def get_leaf_nodes(root, leaf):
    if root is None:
        return
    
    if root.left is None and root.right is None:
        leaf.append(root.value)

    get_leaf_nodes(root.left, leaf)
    get_leaf_nodes(root.right, leaf)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

leaf = []
get_leaf_nodes(root, leaf)
print("Leaf nodes:", leaf)

