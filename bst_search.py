class node:
    def __init__(self,info=None):
        self.data=info
        self.left=None
        self.right=None

def insertion(root,ele):
    if(ele>root.data):
        if(root.right==None):
            root.right=node(ele)
            return
        insertion(root.right,ele)

    elif (ele<root.data):
        if(root.left==None):
            root.left=node(ele)
            return
        insertion(root.left,ele)

def search(root,ele):
    if(root.data==ele):
        print("Found")
        return
    elif (ele>root.data):
        if(root.right==None):
            print("Not found")
            return
        search(root.right,ele)
    elif (ele<root.data):
        if(root.left==None):
            print("Not found")
            return
        search(root.left,ele)
    
lst=[10,14,17,9,5,15,12,7,8,2,3]
root=node(lst[0])
for i in range(1,len(lst)):
    insertion(root,lst[i])
print("Enter the element to be searched in the bst:\n")
ele=int(input())
search(root,ele)
'''if(search(root)==True):
    print("ELement found")
else:
    print("Element not found")'''
