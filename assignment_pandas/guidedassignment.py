# Analyzing a Real Dataset

# Let’s work through a realistic analysis with a sales dataset.

import pandas as pd

sales_data = {
    "date": ["2025-01-05", "2025-01-05", "2025-01-06", "2025-01-06",
             "2025-01-07", "2025-01-07", "2025-01-08", "2025-01-08",
             "2025-01-09", "2025-01-09"],
    "product": ["Widget A", "Widget B", "Widget A", "Widget C",
                "Widget B", "Widget A", "Widget C", "Widget B",
                "Widget A", "Widget C"],
    "quantity": [3, 5, 2, 1, 7, 4, 3, 2, 6, 2],
    "unit_price": [25.99, 15.50, 25.99, 42.00,
                   15.50, 25.99, 42.00, 15.50,
                   25.99, 42.00],
    "region": ["North", "South", "East", "North",
               "West", "South", "East", "North",
               "West", "South"],
}

df = pd.DataFrame(sales_data)

# Step 1: Add a Calculated Column
df["revenue"] = df["quantity"] * df["unit_price"]
print(df.head())

# Step 2: Total Revenue by Product
product_revenue = df.groupby("product")["revenue"].sum().sort_values(ascending=False)
print(product_revenue)

# Step 3: Units Sold by Product
units_by_product = df.groupby("product")["quantity"].sum().sort_values(ascending=False)
print(units_by_product)

# Step 4: Revenue by Region
region_revenue = df.groupby("region")["revenue"].sum().sort_values(ascending=False)
print(region_revenue)

# Step 5: Daily Revenue Trend
daily = df.groupby("date")["revenue"].sum()
print(daily)

#Key Patterns to Remember

    # Add columns: df["new_col"] = expression
    # Filter rows: df[df["col"] > value]
    # Group + aggregate: df.groupby("col")["other_col"].sum()
    # Sort: .sort_values("col", ascending=False)
    # Chain operations: pandas methods return DataFrames, so you can chain them