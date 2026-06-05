# Part 1
# A) O(1) - Constant Time, returns the first element of the list regardless of its size
# B) O(n) - Linear Time, iterates through the entire list to find the target element in the worst case
# C) O(n^2) - Quadratic Time, nested loops iterate through the list
# D) O(log n) - Logarithmic Time, divides the problem in half at each step
# E) O(n log n) - Linearithmic Time, combines linear(O(n)) and logarithmic(O(log n)) behavior

# Part 2
# Write two different functions that both count how many pairs of numbers in a list sum to a given target. One should be O(n²) (nested loops), the other should be O(n) (using a set or dictionary). Benchmark both on lists of size 1,000, 5,000, and 10,000 using the timing pattern from the Guided Example

def has_duplicate_nested(data):
    """Compare every element to every other element."""
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                return True
    return False

def has_duplicate_set(data):
    """Use a set to check for duplicates."""
    seen = set()
    for item in data:
        if item in seen:
            return True
        seen.add(item)
    return False

import time
import random

def benchmark_function(func, data):
    start_time = time.time()
    result = func(data)
    end_time = time.time()
    return end_time - start_time

sizes = [1000, 5000, 10000]

for size in sizes:
    data = list(range(size))
    random.shuffle(data)
    target = random.choice(data)

    t1 = benchmark_function(has_duplicate_nested, data)
    t2 = benchmark_function(has_duplicate_set, data)
    
    print(f"n={size:>6}  |  Nested: {t1:.4f}s  |  Set: {t2:.4f}s")  