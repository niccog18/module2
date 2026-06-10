# Clean and Visualize
# Objective: Apply the full data cleaning pipeline and create meaningful visualizations.

# Tasks:
# 1) Clean it: Stadardize names/regions, convert types, handle missing/invalid values, remove duplicates
# 2) Analyze and visualize: Total sales by product(bar), daily trend(line), distribution(histogram).
# 3) Save visualizations to a PNG file with at least 2 charts.

import pandas as pd
import matplotlib.pyplot as plt

# The Data
messy = pd.DataFrame({
    "product": ["Widget A", "Widget B", "widget a", "Widget C", "Widget B",
                "Widget A", " Widget C", "Widget D", None, "Widget A"],
    "sales": ["150", "200", "175", "300", "200",
              "180", "250", "abc", "100", "-50"],
    "date": ["2025-01-01", "2025-01-01", "2025-01-02", "2025-01-02", "2025-01-03",
             "2025-01-03", "2025-01-04", "2025-01-04", "2025-01-05", "2025-01-05"],
    "region": ["North", "South", "north", "East", "South",
               "West", "east", "North", "South", "West"],
})

# 1) Clean it
df = pd.DataFrame(messy)
print("\n=== Raw Data ===")
print(df)
print(f"\nShape: {df.shape}")
print(f"\nMissing values:\n{df.isnull().sum()}")
print(f"\nDuplicates:\n{df.duplicated().sum()}")

# Step 1: 
# Standardize names
df["product"] = df["product"].str.strip().str.title()
df["region"] = df["region"].str.strip().str.title()

# Convert types
df["sales"] = pd.to_numeric(df["sales"], errors="coerce")
df["date"] = pd.to_datetime(df["date"], errors="coerce")


# Handle missing/invalid values
df = df.dropna(subset=["product"])
df.loc[df["sales"] < 0, "sales"] = pd.NA

# Remove duplicates
df = df.drop_duplicates()

print("\n=== Clean Data ===")
print(df)

# Step 2: Analyze/Visualize
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Bar Graph
product_sales = df.groupby("product")["sales"].sum()
product_sales.plot(kind="bar", ax=axes[0])
plt.xlabel("Product")
plt.ylabel("Total Sales")
axes[0].set_title("Total Sales by Product")

# Line Graph
daily_sales = df.groupby("date")["sales"].sum()
daily_sales.plot(kind="line", marker="o", ax=axes[1])
plt.xlabel("Date")
plt.ylabel("Daily Sales")
axes[1].set_title("Daily Sales Trend")

# Histogram
axes[2].hist(df["sales"].dropna(), bins=5)
plt.xlabel("Sales Amount")
plt.ylabel("Frequency")
axes[2].set_title("Sales Distribution")

# Step 3: Save to PNG
plt.tight_layout()
plt.savefig("sales_summary.png", dpi=150)
plt.show()

print("\n=== Summary ===")

# Total sales
total_sales = df["sales"].sum()

# Best-selling product
top_product = product_sales.idxmax()
top_product_sales = product_sales.max()

# Highest sales day
top_day = daily_sales.idxmax()
top_day_sales = daily_sales.max()

# Average sale amount
avg_sale = df["sales"].mean()

print(f"Total sales: {total_sales:.0f}")
print(f"Top product: {top_product} (${top_product_sales:.0f})")
print(f"Highest sales day: {top_day.date()} (${top_day_sales:.0f})")
print(f"Average sale amount: ${avg_sale:.2f}")