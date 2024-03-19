class Node:
  def __init__(self, data) -> None:
    self.data = data
    self.left = None
    self.right = None

def kth_smallest_element_in_BST(root, k):
  arr = []
  def inorder(root):
    if root == None:
      return
    inorder(root.left)
    arr.append(root.data)
    inorder(root.right)
  inorder(root)
  return arr[k-1]

if __name__ == "__main__":
  root1, root2 = Node(20), Node(25)

  root1.left = Node(8)
  root1.left.left = Node(4)
  root1.left.right = Node(12)
  root1.left.right.left = Node(10)
  root1.left.right.right = Node(14)
  root1.right = Node(22)

  root2.left = Node(20)
  root2.right = Node(36)
  root2.left.left = Node(10)
  root2.left.right = Node(22)
  root2.left.left.left = Node(5)
  root2.left.left.right = Node(12)
  root2.left.left.left.left = Node(1)
  root2.left.left.left.right = Node(8)
  root2.left.left.right.right = Node(15)
  root2.right.left = Node(30)
  root2.right.right = Node(40)
  root2.right.left.left = Node(28)
  root2.right.right.left = Node(38)
  root2.right.right.right = Node(48)
  root2.right.right.right.left = Node(45)
  root2.right.right.right.right = Node(50)

  testcase = [root1, root2]
  r = int(input("Enter Tree (1/2): "))
  k = int(input(f"Enter k: "))
  print(kth_smallest_element_in_BST(testcase[r-1], k))