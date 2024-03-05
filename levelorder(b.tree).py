

class node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None

def levelOrder(root):
  queue = [root]
  queue.append(None)

  while len(queue)>0:
    cur = queue.pop(0)

    if cur is None:
      print()
      if len(queue)>0:
        queue.append(None)

    else:
      print(cur.data, end=" ")

      if cur.left:
        queue.append(cur.left)

      if cur.right:
        queue.append(cur.right)

# Sample usage
root = node(20)
root.left = node(32)
root.right = node(10)

levelOrder(root)
