# Functional Data Processor
# Objective: Process a dataset using only functional patterns

# The Data
products = [
    {"name": "Laptop", "price": 999.99, "category": "electronics", "in_stock": True},
    {"name": "Python Book", "price": 39.99, "category": "books", "in_stock": True},
    {"name": "Headphones", "price": 149.99, "category": "electronics", "in_stock": False},
    {"name": "Desk Lamp", "price": 29.99, "category": "home", "in_stock": True},
    {"name": "AI Textbook", "price": 89.99, "category": "books", "in_stock": True},
    {"name": "Monitor", "price": 349.99, "category": "electronics", "in_stock": True},
    {"name": "Notebook", "price": 4.99, "category": "office", "in_stock": True},
    {"name": "Keyboard", "price": 79.99, "category": "electronics", "in_stock": False},
]

# Tasks: Using list comprehensions, map, filter, and/or lambda:

# Get all in-stock products (filter)
# Add a "discounted_price" field that’s 10% off the original (map - create new dicts, don’t mutate)
# Get only electronics under $200 (filter with two conditions)
# Sort all products by price, lowest first (use sorted with a key lambda)
# Calculate the total value of all in-stock products (reduce or sum with comprehension)
# Group products by category, return a dictionary like {"electronics": [...], "books": [...], ...}

# Rules: Do not use for loops with append. Use comprehensions or functional tools only. Do not modify the original products list.

# Step 1: Get all in-stock products (filter)
def in_stock(product):
    """Return True if the product is in stock."""
    return product["in_stock"]

in_stock_products = list(filter(in_stock, products))

# Step 2: Add a "discounted_price" field that’s 10% off the original (map - create new dicts, don’t mutate)
def add_discount(product):
    """Return a new dict with a discounted_price field."""
    return {**product, "discounted_price": product["price"] * 0.9}

discounted_products = list(map(add_discount, products))

# Step 3: Get only electronics under $200 (filter with two conditions)
def is_electronics_under_200(product):
    """Return True if product is an electronic item under $200."""
    return product["category"] == "electronics" and product["price"] < 200

electronics_under_200 = list(filter(is_electronics_under_200, products))

# Step 4: Sort all products by price, lowest first (use sorted with a key lambda)
sorted_products = sorted(products, key=lambda x: x["price"])

# Step 5: Calculate the total value of all in-stock products (reduce or sum with comprehension)
total_value = sum(p["price"] for p in filter(in_stock, products))

# Step 6: Group products by category, return a dictionary like {"electronics": [...], "books": [...], ...}
grouped_products = {category: [product for product in products if product["category"] == category] for category in set(product["category"] for product in products)}
def group_by_category(products):
    """Return a dict grouping products by their category."""
    categories = set(product["category"] for product in products)
    return {category: [product for product in products if product["category"] == category] for category in categories}

grouped_products = group_by_category(products)

#Summarize results:
print("In-stock products:")
for product in in_stock_products:
    print(f" - {product['name']}: ${product['price']:.2f}")

print(f"Total value of in-stock products: ${total_value:.2f}")

print("Electronics under $200:")
for product in electronics_under_200:
    print(f" - {product['name']}: ${product['price']:.2f}")

print("Products sorted by price:")
for product in sorted_products:
    print(f" - {product['name']}: ${product['price']:.2f}")

print("Grouped products by category:")
for category, products_list in grouped_products.items():
    print(f" - {category.capitalize()}:")
    for product in products_list:
        print(f"   * {product['name']}: ${product['price']:.2f}")


