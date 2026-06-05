# Build and Use

# Objective: Implement data structures and use them to solve practical problems.

from collections import deque

# Part 1: Extend the Linked List
# Start from the LinkedList in linkedlist.py, add these methods:
class Node:
    """A single node in a linked list."""

    def __init__(self, value):
        self.value = value   # The data this node holds
        self.next = None     # Reference to the next node (None if this is the last)

    def __repr__(self):
        return f"Node({self.value})"

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

    def delete(self, target):
        """Remove the first node with the given value. Return True if found, False if not."""
        if self.head is None:
            return False

        if self.head.value == target:
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next.value == target:
                current.next = current.next.next
                return True
            current = current.next

        return False

    def length(self):
        """Return the number of nodes in the list. O(n) time."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def to_list(self):
        """Convert the linked list to a Python list. Returns a list of values."""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

# Test your methods:
ll = LinkedList()
for value in [10, 20, 30, 40, 50]:
    ll.insert_at_end(value)

ll.display()           # 10 -> 20 -> 30 -> 40 -> 50 -> None
print(ll.length())     # 5
ll.delete(30)
ll.display()           # 10 -> 20 -> 40 -> 50 -> None
print(ll.to_list())    # [10, 20, 40, 50]

# Part 2 - Stack: Bracket Validator

# Write a function that checks whether a string of brackets is properly balanced using a stack:

def is_balanced(text):
    """Return True if all brackets in text are properly matched.
    Handles: (), [], {}
    """
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in text:
        if char in pairs.values():  # If it's an opening bracket
            stack.append(char)
        elif char in pairs:         # If it's a closing bracket
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()  # Pop the matching opening bracket

    return len(stack) == 0  # True if no unmatched opening brackets remain

# Tests:
print(is_balanced("()"))           # True
print(is_balanced("({[]})"))       # True
print(is_balanced("(]"))           # False
print(is_balanced("([)]"))         # False
print(is_balanced("hello (world)")) # True

# Part 3 - Queue: Task Processor

# Using collections.deque, simulate a simple task processor. Write a TaskProcessor class with add_task(name) and process_next() methods. process_next() should return the oldest unprocessed task (FIFO) or None if empty.
class TaskProcessor:
    """A simple task processor using a queue (deque)."""

    def __init__(self):
        self.tasks = deque()

    def add_task(self, name):
        """Add a new task to the processor."""
        self.tasks.append(name)

    def process_next(self):
        """Process and return the next task in the queue. Returns None if no tasks are available."""
        if self.tasks:
            return self.tasks.popleft()
        return None
    
# Test the TaskProcessor
processor = TaskProcessor()
processor.add_task("Blue")
processor.add_task("Green")
processor.add_task("Red")
print(processor.process_next())  # Blue
print(processor.process_next())  # Green
print(processor.process_next())  # Red
print(processor.process_next())  # None (no more tasks)