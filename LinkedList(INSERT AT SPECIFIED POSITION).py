class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        for _ in range(position - 2):
            if current is None:
                print("Position out of range")
                return
            current = current.next
        
        if current is None:
            print("Position out of range")
            return
        
        new_node.next = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
if __name__ == "__main__":
    # Create a new linked list
    linked_list = LinkedList()

    # Insert some nodes at the beginning
    linked_list.insert_at_position(3, 1)
    linked_list.insert_at_position(7, 2)
    linked_list.insert_at_position(1, 2)
    linked_list.insert_at_position(9, 4)

    # Print the linked list
    linked_list.print_list()
