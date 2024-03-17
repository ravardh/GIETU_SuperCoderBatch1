# Python code

class AVL:
	def __init__(self, data = None):
		self.left = None
		self.right = None
		self.data = data
		self.par = None
		self.height = 1
  
def update_height(root):
  if root is not None:
    left_height = root.left.height if root.left else 0  # Get the height of the left child
    right_height = root.right.height if root.right else 0  # Get the height of the right child
    root.height = max(left_height, right_height) + 1  # Update the height of the current node

def LLR(root):
  # Perform a left rotation and then a right rotation
  tmpnode = root.left
  root.left = tmpnode.right
  if tmpnode.right:
    tmpnode.right.par = root
  tmpnode.right = root
  tmpnode.par = root.par
  root.par = tmpnode
  if tmpnode.par:
    if root.data < tmpnode.par.data:
      tmpnode.par.left = tmpnode
    else:
      tmpnode.par.right = tmpnode
  update_height(root)
  update_height(tmpnode)
  return tmpnode

def RRR(root):
    # Perform a right rotation and then a left rotation
    tmpnode = root.right
    root.right = tmpnode.left
    if tmpnode.left:
        tmpnode.left.par = root
    tmpnode.left = root
    tmpnode.par = root.par
    root.par = tmpnode
    if tmpnode.par:
        if root.data < tmpnode.par.data:
            tmpnode.par.left = tmpnode
        else:
            tmpnode.par.right = tmpnode
    update_height(root)
    update_height(tmpnode)
    return tmpnode
 
def LRR(root):
  # Perform a right rotation on the left child and then a left rotation on the root
  root.left = RRR(root.left)
  return LLR(root)

def RLR(root):
  # Perform a left rotation on the right child and then a right rotation on the root
  root.right = LLR(root.right)
  return RRR(root)

def insert(root, parent, data):
  if root is None:
    root = AVL(data)
    root.par = parent
  elif root.data > data:
    # Insert the data into the left subtree and balance the tree if needed
    root.left = insert(root.left, root, data)
    left_height = root.left.height if root.left else 0
    right_height = root.right.height if root.right else 0
    if abs(left_height - right_height) == 2:
      if data < root.left.data:
        root = LLR(root)
      else:
        root = LRR(root)
  elif root.data < data:
    # Insert the data into the right subtree and balance the tree if needed
    root.right = insert(root.right, root, data)
    left_height = root.left.height if root.left else 0
    right_height = root.right.height if root.right else 0
    if abs(left_height - right_height) == 2:
      if data < root.right.data:
        root = RLR(root)
      else:
        root = RRR(root)
  update_height(root)
  return root  

def avl_search(root, data):
  if root is None:
    return False
  elif root.data == data: 
    return True
  elif root.data > data:  # traverse left
    return avl_search(root.left, data)
  else: # traverse right
    return avl_search(root.right, data)

def preorder(root):
  if root == None:
    return
  
  print(root.data, end=" | ")
  preorder(root.left)
  preorder(root.right)

def levelorder(root):
  q=[root]
  q.append(None)
  i=1
  print(f"\nLevel {i}")
  while len(q)>0:
    curr = q.pop(0)
    if curr == None:
      i += 1
      if len(q) > 0:
        print(f"\nLevel {i}")
        q.append(None)
    else:
      print(curr.data, end=" | ")
      if curr.left != None:
        q.append(curr.left)
      if curr.right != None:
        q.append(curr.right)

arr = [20, 32, 15, 12, 4, 50, 6, 40, 35, 10, 8, 24, 16, 2]
root = None
for i in arr:
  root = insert(root, None, i)

print("Pre Order")
preorder(root)
print()
print("Level Order")
levelorder(root)

print("Value found" if avl_search(root, int(input("\nEnter Key: "))) else "Not found!")