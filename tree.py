class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def preorder(root):
    if root is None:
        return None
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return None
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
    
def postorder(root):
    if root is None:
        return None
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")
    
def levelorder(root):
    queue=[]
    queue.append(root)
    queue.append(None)
    while len(queue)>1:
        front=queue.pop(0)
        if front is not None:
            print(front.data,end=" ")
            if front.left!=None:
                queue.append(front.left)
            if front.right!=None:
                queue.append(front.right)
        else:
            print()
            queue.append(None)
            
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.right.right=TreeNode(5)
print("Preorder Traversal:")
preorder(root)
print()
print("Inorder Traversal:")
inorder(root)
print()
print("Postorder Traversal:")
postorder(root)
print()
print("Levelorder Traversal:")
levelorder(root)