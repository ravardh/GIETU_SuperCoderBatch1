#Height of a binary tree
class node:
  def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None
def findheight(root):
  if(root==None):
   return 0;
  return max(findheight(root.left),findheight(root.right))+1
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)
root.left.left.right=node(8)
root.left.left.left=node(9)
root.left.left.right.left=node(10)
root.left.left.right.right=node(11)
print(findheight(root))
findheight(root)

# Leaf Nodes

class Node:
    def _init_(self,data):
        self.data = data
        self.left = None
        self.right = None

def printLeafNodes(root:Node) -> None:
    if root == None:
        return

    if root.left == None and root.right == None:
        print(root.data,end = " ")
        return

    if root.left:
        printLeafNodes(root.left)

    if root.right:
        printLeafNodes(root.right)

# Driver Code
if _name_ == "_main_":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(8)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)
    root.right.right.left = Node(9)
    root.right.right.right = Node(10)
    
    print("Leaf Nodes : ")
    printLeafNodes(root)


#top view
class Node:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.key = None
def topview(root):
  if(root==None):
    return
  Q=[root]
  key=0
  TView=dict()
  root.key=key
  while len(Q)!=0:
    cur = Q.pop(0)
    key = cur.key
    if cur.left!=None:
      Q.append(cur.left)
      cur.left.key=key-1
    if cur.right!=None:
      Q.append(cur.right)
      cur.right.key=key+1
  for x in sorted(TView.keys()):
    print(TView[x],end=" ")
root = Node(20)
root.left = Node(32)
root.right = Node(10)
root.left.left = Node(15)
root.left.right = Node(12)
root.right.left = Node(8)
root.right.right = Node(24)
root.left.left.right = Node(4)
root.left.left.left = Node(9)
root.left.right.left = Node(50)
root.left.right.right = Node(6)
root.left.right.left.left = Node(40)
root.left.right.left.right = Node(35)
root.right.right.left = Node(16)
root.right.right.right = Node(2)
topview(root)


# Bottom View

class Node:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.key = None

def bottomView(root):
    if root == None:
        return
    
    Q = [root]
    key = 0
    BV = dict()
    root.key = key
    
    while len(Q) != 0:
        cur = Q.pop(0)
        key = cur.key
        BV[key] = cur.data
        
        if cur.left != None:
            Q.append(cur.left)
            cur.left.key = key - 1
        
        if cur.right != None:
            Q.append(cur.right)
            cur.right.key = key + 1
    
    for i in sorted(BV.keys()):
        print(BV[i], end = " ")

root = Node(9)

root.left = Node(7)
root.right = Node(1)

root.left.left = Node(6)
root.left.right = Node(4)
root.right.left = Node(3)
root.right.right = Node(2)

root.left.left.right = Node(5)
root.right.left.left = Node(11)
root.right.left.right = Node(12)

root.right.left.right.right = Node(17)

print("Bottom View :")
bottomView(root)
