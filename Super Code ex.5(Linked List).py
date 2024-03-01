#Linked List:
class node:
    def __init__(self,data = None):
        self.data= data
        self.next= None
n1 = node(1)
n2 = node(2)
n3 = node(3)
n4 = node(4)
n5 = node(5)
n6 = node(6)
start = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
print(start)
current = n1
while(current):
    print(current.data)
    current = current.next
