# Data Transformation Pipeline

# Let’s build a data processing workflow using functional patterns, the kind of operations you’ll do constantly with pandas and in your AI engineering work.
# The Data

students = [
    {"name": "Alice Johnson", "grade": 92, "status": "active"},
    {"name": "bob smith", "grade": 55, "status": "active"},
    {"name": "Charlie Brown", "grade": 78, "status": "inactive"},
    {"name": "diana prince", "grade": 88, "status": "active"},
    {"name": "Eve Wilson", "grade": 45, "status": "active"},
    {"name": "Frank Castle", "grade": 71, "status": "inactive"},
    {"name": "grace hopper", "grade": 99, "status": "active"},
]

# Step 1: Clean names (map)
def clean_name(student):
    """Return a new dict with the name title-cased. Does NOT modify the original."""
    return {**student, "name": student["name"].title()}

cleaned = [{**s, "name": s["name"].title()} for s in students]

# Notice: {**student, "name": ...} creates a new dictionary with all the same keys plus the updated name. The original students list is untouched. This is the functional pattern, transform, don’t mutate.

# Step 2: Filter active students only
active = [s for s in cleaned if s["status"] == "active"]
# 5 students remain (Charlie and Frank are inactive)

# Step 3: Classify pass/fail (map)
def classify(student):
    """Add a 'result' field based on grade."""
    return {**student, "result": "pass" if student["grade"] >= 60 else "fail"}

classified = [classify(s) for s in active]

# Step 4: Summarize (reduce)
from functools import reduce

total = reduce(lambda acc, s: acc + s["grade"], classified, 0)
avg = total / len(classified)
print(f"Average grade (active): {avg:.1f}")  # 75.8

passing = len([s for s in classified if s["result"] == "pass"])
failing = len(classified) - passing
print(f"Passing: {passing}, Failing: {failing}")  # Passing: 3, Failing: 2

# The Full Pipeline - Chained Together
result = (
    [classify({**s, "name": s["name"].title()})
     for s in students
     if s["status"] == "active"]
)

for student in result:
    print(f"  {student['name']}: {student['grade']} ({student['result']})")


# Output:
#  Alice Johnson: 92 (pass)
#  Bob Smith: 55 (fail)
#  Diana Prince: 88 (pass)
#  Eve Wilson: 45 (fail)
#  Grace Hopper: 99 (pass)