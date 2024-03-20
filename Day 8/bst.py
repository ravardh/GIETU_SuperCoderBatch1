import sys
sys.path.append('..\Day 6')  # Add Day8 directory to Python path

from tree_traversal import Node, levelorder, inorder, root

def insert(root, data):
  if root is None:
    return Node(data)
  else:
    if root.data == data:
      return root
    elif root.data < data:
      root.right = insert(root.right, data)
    else:
      root.left = insert(root.left, data)
    return root

def search(root, key):
  if root is None or root.data == key:
    return root
  if root.data < key:
    return search(root.right, key)
  return search(root.left, key)

if __name__ == "__main__":
    r = root
    arr = []
    def inorder(root):
      if root == None:
        return
      inorder(root.left)
      arr.append(root.data)
      inorder(root.right)
    inorder(r)
    print(*arr)
    bst = Node(20)
    for i in arr:
      bst = insert(bst, i)
    arr = []
    inorder(bst)
    print(*arr)
    # print BST
    levelorder(bst)
    print()
    inorder(bst)  # to verify the sorted nature
    print()
    x = search(bst, int(input("Enter Key: ")))
    print("Found" if x is not None else "Not Found")
