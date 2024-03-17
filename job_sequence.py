class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def nodeCreation():
    head = None
    temp = None
    n = int(input("Enter the data for node: ")) 
    while n != -1:
        if head is None:
            head = Node(n)
            temp = head
        else:
            temp.next = Node(n)
            temp = temp.next
        n = int(input("Enter the data for node (enter -1 to exit): ")) 
    return head

def insertNodeAtBeginning(head):
    data=int(input("Enter the data: "))
    newNode=Node(data)
    if head is None:
        head=newNode
    else:
        newNode.next=head
        head=newNode
    return head

def insertNodeAtLast(head):
    data=int(input("Enter the data: "))
    temp=head
    while temp.next!=None:
        temp=temp.next
    temp.next=Node(data)

def printLL(head):
    temp=head
    while temp!=None:
        print(temp.data)
        temp=temp.next

def insertNodeAtPosition(head):
    pos=int(input("Enter the position(index): "))
    data=int(input("Enter the data"))
    newNode=Node(data)
    temp=head
    k=0
    if pos==0:
        newNode.next=head
        head=newNode
        return head
    else:
        while k<pos-1:
            temp=temp.next
            k=k+1
        if k==pos-1:
            newNode.next=temp.next
            temp.next=newNode
    return head

def deleteNodeFromBeginning(head):
    temp=head
    if head is None:
        print("Deletion can't be done")
    else:
        print("The deleted node is: ",temp.data)
        temp=temp.next
        head=temp
    return head

def deleteNodeFromLast(head):
    temp=head
    while temp.next.next!=None:
        temp=temp.next
    print("The deleted node is: ",temp.next.data)
    temp.next=None

def deleteNodeFromApos(head):
    pos=int(input("Enter the position(index): "))
    temp=head
    k=0
    if pos==0:
        head=head.next
        return head
    else:
        while k<pos:
            prev=temp
            temp=temp.next
            k=k+1
        print("The deleted node is: ",temp.data)
        prev.next=temp.next
        temp.next=None
    return head

print("Nodes Creation(Inserting data in a linked list)")
head=nodeCreation()
while True:
    print("1. Insert a Node at Beginning")
    print("2. Insert a Node At End")
    print("3. Insert a Node at a Specific Position")
    print("4. Delete a Node from Beginning")
    print("5. Delete a Node from End")
    print("6. Delete a Node from a Specific Position")
    print("7. Print the list")
    print("8. Exit")
    print()
    print()
    x=int(input("Enter your choice: "))
    
    match x:
        case 1:
            head=insertNodeAtBeginning(head)
            print()
        case 2:
            insertNodeAtLast(head)
            print()
        case 3:
            head=insertNodeAtPosition(head)
            print()
        case 4:
            head=deleteNodeFromBeginning(head)
            print()
        case 5:
            deleteNodeFromLast(head)
            print()
        case 6:
            head=deleteNodeFromApos(head)
            print()
        case 7:
            printLL(head)
            print()
        case 8:
            break
        case _:
            print("Invalid operator")