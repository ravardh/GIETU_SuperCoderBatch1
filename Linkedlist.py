# Creation of linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
#Insertion at begining
        
def insertAtBegin(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    else:
        new_node.next = self.head
        self.head = new_node
        
# Insertion at specific psition

def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
 
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")
                
# Insertion at end

def inserAtEnd(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
 
    current_node = self.head
    while(current_node.next):
        current_node = current_node.next
 
    current_node.next = new_node
    
# Deletion at begining

def remove_first_node(self):
    if(self.head == None):
        return
     
    self.head = self.head.next
    
# Deletion at last

def remove_last_node(self):
 
    if self.head is None:
        return
 
    current_node = self.head
    while(current_node.next.next):
        current_node = current_node.next
 
    current_node.next = None
    
# Deletion from specific position

def remove_at_index(self, index):
        if self.head == None:
            return
 
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")