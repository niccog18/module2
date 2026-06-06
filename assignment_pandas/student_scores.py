# Student Scores Analysis

# OBjective: Load, explore, filter and analyze a dataset using pandas.

# The Data
data = {
    "student": ["Alice", "Bob", "Charlie", "Diana", "Eve",
                 "Frank", "Grace", "Henry", "Iris", "Jack"],
    "course": ["Python", "Python", "SQL", "SQL", "Python",
               "SQL", "Python", "SQL", "Python", "SQL"],
    "score": [92, 78, 85, 91, 88, 72, 95, 68, 84, 90],
    "hours_studied": [20, 12, 18, 22, 15, 8, 25, 10, 16, 19],
    "passed": [True, True, True, True, True, False, True, False, True, True],
}

# Questions(answer using pandas, not loops):
# 1) How many students are in each course?
# 2) What is the average score per course?
# 3) Who are the top 3 students by score?
# 4) What is the average hours studied for students who passed vs. didn't pass?
# 5) Create a "grade" column: 90+ = "A", 80-89 = "B", 70-79 = "C", below 70 = "F".
# 6) What's the distribution of grades per course?

import pandas as pd

df = pd.DataFrame(data)

# 1) How many students are in each course?
course_counts = df.groupby("course").size()
print("\n=== Number of Students in Each Course ===")
print(course_counts)

# 2) What is the average score per course?
avg_score = df.groupby("course")["score"].mean()
print("\n=== Average Score per Course ===")
print(avg_score)

# 3) Who are the top 3 students by score?
top_students = df.nlargest(3, "score")
print("\n=== Top 3 Students by Score ===")
print(top_students)

# 4) What is the average hours studied for students who passed vs. didn't pass?
avg_hours = df.groupby("passed")["hours_studied"].mean()
print("\n=== Average Hours Studied (Passed vs. Not Passed) ===")
print(avg_hours)

# 5) Create a "grade" column: 90+ = "A", 80-89 = "B", 70-79 = "C", below 70 = "F".
df["grade"] = pd.cut(
    df["score"],
    bins=[0, 70, 80, 90, 101],
    labels=["F", "C", "B", "A"],
    right=False,
    include_lowest=True,
)
print("\n=== DataFrame with Grade Column ===")
print(df)

# 6) What's the distribution of grades per course?
grade_distribution = df.groupby(["course", "grade"]).size().unstack(fill_value=0)
print("\n=== Distribution of Grades per Course ===")
print(grade_distribution)