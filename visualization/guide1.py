# Cleaning and Visualizing a Messy Dataset
# Step 1: Load and Inspect
import pandas as pd
import matplotlib.pyplot as plt

messy_data = {
    "name": ["Alice", "Bob", "Charlie", "  Diana  ", "Eve", "Bob", "Frank", None, "Grace", "Henry"],
    "department": ["Engineering", "marketing", "ENGINEERING", "Sales", "engineering",
                   "marketing", "Sales", None, "Engineering", "sales"],
    "salary": ["95000", "72000", "110000", "68000", "88000",
               "72000", "75000", "82000", "-5000", "78000"],
    "start_date": ["2020-03-15", "2022-01-10", "2018-07-22", "2024-06-01", "2021-11-30",
                   "2022-01-10", "2023-03-15", "2020-08-01", "not a date", "2023-09-15"],
    "email": ["alice@co.com", "bob@co.com", "charlie@co.com", "diana@co.com", "eve@co.com",
              "bob@co.com", "frank@co.com", "unknown@co.com", "grace@co.com", "henry@co.com"],
}

df = pd.DataFrame(messy_data)
print("=== Raw Data ===")
print(df)
print(f"\\nShape: {df.shape}")
print(f"\\nMissing values:\\n{df.isnull().sum()}")

# Step 2: Clean the Data
# 1. Fix whitespace in names
df["name"] = df["name"].str.strip()

# 2. Standardize department names
df["department"] = df["department"].str.strip().str.title()

# 3. Convert salary to numeric
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

# 4. Convert dates (invalid dates become NaT)
df["start_date"] = pd.to_datetime(df["start_date"], errors="coerce")

# 5. Remove duplicates (Bob appears twice)
df = df.drop_duplicates(subset=["email"], keep="first")

# 6. Handle missing values
df = df.dropna(subset=["name"])
df["department"] = df["department"].fillna("Unknown")

# 7. Fix invalid values
df.loc[df["salary"] < 0, "salary"] = pd.NA

print("\\n=== Clean Data ===")
print(df)

# Step 3: Visualize the Data
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Chart 1: Headcount by department
dept_counts = df["department"].value_counts()
axes[0].bar(dept_counts.index, dept_counts.values, color="steelblue")
axes[0].set_title("Employees by Department")
axes[0].set_ylabel("Count")
axes[0].tick_params(axis="x", rotation=45)

# Chart 2: Salary distribution
df["salary"].dropna().hist(ax=axes[1], bins=6, color="coral", edgecolor="black")
axes[1].set_title("Salary Distribution")
axes[1].set_xlabel("Salary ($)")
axes[1].set_ylabel("Count")

# Chart 3: Average salary by department
avg_salary = df.groupby("department")["salary"].mean().sort_values(ascending=False)
axes[2].barh(avg_salary.index, avg_salary.values, color="seagreen")
axes[2].set_title("Avg Salary by Department")
axes[2].set_xlabel("Salary ($)")

plt.tight_layout()
plt.savefig("employee_analysis.png", dpi=150)
plt.show()


