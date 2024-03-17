class Node:
  def __init__(self, data=None) -> None:
    self.data = data
    self.left = None
    self.right = None

def preorder(root: Node) -> None: # Root, Left, Right
  if root == None:
    return
  
  print(root.data, end=" | ")
  preorder(root.left)
  preorder(root.right)

def inorder(root: Node) -> None: # Left, Root, Right
  if root == None:
    return
  
  inorder(root.left)
  print(root.data, end=" | ")
  inorder(root.right)

def postorder(root: Node) -> None: # Left, Right, Root
  if root == None:
    return
  
  postorder(root.left)
  postorder(root.right)
  print(root.data, end=" | ")

''' Level Order Algo [BFS]
Use Queue DS
Initially add root and None
While removing any node add all it's child
While removing None Print new line and add None again
'''
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

root = Node(20)

root.left = Node(32)
root.left.left = Node(15)
root.left.right = Node(12)
root.left.left.left = Node(4)
root.left.right.left = Node(50)
root.left.right.right = Node(6)
root.left.right.left.left = Node(40)
root.left.right.left.right = Node(35)

root.right = Node(10)
root.right.left = Node(8)
root.right.right = Node(24)
root.right.right.left = Node(16)
root.right.right.right = Node(2)

if __name__ == "__main__":

  print("Pre Order [Root, Left, Right]")
  preorder(root)

  print("\nIn Order [Left, Root, Right]")
  inorder(root)

  print("\nPost Order [Left, Right, Root]")
  postorder(root)

  print("\nLevel Order [BFS]")
  levelorder(root)
