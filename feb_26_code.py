class node:
  def _init_(self, info = None):
    self.data = info
    self.left = None
    self.right = None

def preorder(root):
  if root == None:
    return
  print(root.data,end = " ")
  preorder(root.left)
  preorder(root.right)

def inorder(root):
  if root == None:
    return
  inorder(root.left)
  print(root.data,ends = " ")
  inorder(root.right)

def postorder(root):
  if root == None:
    return
  postorder(root.left)
  postorder(root.right)
  print(root.data,ends = " ")

def levelorder(root):
    Q =[root]
    Q.append(None)
    while len(Q)>0:
      cur = Q.pop(0)
      if cur==None:
        print()
        if len(Q)>0:
          Q.append(None)
      else:
        print(cur.data,end=" ")
        if cur.left!=None:
          Q.append(cur.left)
        if cur.right!=None:
          Q.append(cur.right)
  
    
root = node(20)
root.left = node(32)
root.right = node(10)

root.left.left = node(15)
root.left.right = node(12)
root.right.left = node(8)
root.right.right = node(24)

root.left.left.left = node(4)
root.left.right.left = node(50)
root.left.right.right = node(6)
root.right.right.left = node(16)
root.right.right.right = node(2)

root.left.right.left.left = node(40)
root.left.right.left.right = node(35)

print(root)
print(root.data)
print("Preorder Traversal")
preorder(root)
print("\nInorder Traversal")
preorder(root)
print("\nPostorder Traversal")
preorder(root)
print("\nLevelorder Traversal")
levelorder(root)