# Stacks and Queues in Python

# Stack (using a list)

# A stack is just a list where you only use append() and pop()

stack = []

stack.append("page_1")    # Push: visit page 1
stack.append("page_2")    # Push: visit page 2
stack.append("page_3")    # Push: visit page 3

print(stack)               # ['page_1', 'page_2', 'page_3']

back = stack.pop()         # Pop: go back
print(back)                # 'page_3' — the most recent page
print(stack)               # ['page_1', 'page_2']

# Queue (using collections.deque)
from collections import deque

queue = deque()

queue.append("customer_1")   # Enqueue: customer 1 joins the line
queue.append("customer_2")   # Enqueue: customer 2 joins the line
queue.append("customer_3")   # Enqueue: customer 3 joins the line

print(queue)                  # deque(['customer_1', 'customer_2', 'customer_3'])

served = queue.popleft()      # Dequeue: serve the first customer
print(served)                 # 'customer_1' — first in, first out
print(queue)                  # deque(['customer_2', 'customer_3'])