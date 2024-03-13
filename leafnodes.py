class Node:
   
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLeafNodes(root: Node) -> None:
 
    if (not root):
        return
 

    if (not root.left and
        not root.right):
        print(root.data, 
              end = " ")
        return
 

    if root.left:
        printLeafNodes(root.left)

    if root.right:
        printLeafNodes(root.right)
 
if __name__ == "__main__":
 

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
 
    printLeafNodes(root)
 