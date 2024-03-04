class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

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

    # Insert some nodes at the end
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(7)
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(9)

    # Print the linked list
    linked_list.print_list()
