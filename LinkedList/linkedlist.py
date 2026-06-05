# Building a Linked List from Scratch

#Step 1: Define the Node
# Each node holds a value and a pointer to the next node.

class Node:
    """A single node in a linked list."""

    def __init__(self, value):
        self.value = value   # The data this node holds
        self.next = None     # Reference to the next node (None if this is the last)

    def __repr__(self):
        return f"Node({self.value})"
    
# Step 2: Define the LinkedList
# The linked list itself just needs to know where the chain starts, the head node.
class LinkedList:
    """A singly linked list."""

    def __init__(self):
        self.head = None  # The list starts empty

    def insert_at_beginning(self, value):
        """Add a new node at the front of the list. O(1) time."""
        new_node = Node(value)
        new_node.next = self.head  # New node points to the old head
        self.head = new_node       # New node becomes the new head

    def insert_at_end(self, value):
        """Add a new node at the end of the list. O(n) time — must traverse to the end."""
        new_node = Node(value)
        if self.head is None:      # List is empty
            self.head = new_node
            return
        current = self.head
        while current.next:        # Walk to the last node
            current = current.next
        current.next = new_node    # Last node now points to the new node

    def search(self, target):
        """Find a value in the list. Returns True/False. O(n) time."""
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next  # Follow the pointer to the next node
        return False

    def display(self):
        """Print the list in a readable format."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" -> ".join(elements) + " -> None")

# Step 3: Example usage
# Create a linked list and add some values
my_list = LinkedList()
my_list.insert_at_beginning(3)
my_list.insert_at_beginning(2)
my_list.insert_at_beginning(1)
my_list.insert_at_end(4)

my_list.display()
# Output: 1 -> 2 -> 3 -> 4 -> None

print(my_list.search(3))   # True
print(my_list.search(99))  # False
