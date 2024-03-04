#LEFT VIEW OF TREE USING RECURSIVE :
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def leftViewUtil(root,level,max_level):
    if root is None:
        return
    if(max_level[0]< level):
        print(root.data,end=' N')
        max_level[0]=level
    leftViewUtil(root.left,level+1,max_level)
    leftViewUtil(root.right,level+1,max_level)
def leftView(root):
    max_level = [0]
    leftViewUtil(root,1,max_level)
if __name__ == '__main__':

    root = Node(20)
    root.left = Node(18)
    root.right = Node(35)
    root.left.left = Node(12)
    root.left.right = Node(9)
    root.right.left = Node(42)
    root.right.right = Node(38)
    root.left.left.right = Node(5)
    root.right.left.right = Node(90)

    leftView(root)


