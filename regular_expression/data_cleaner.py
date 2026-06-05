# The Data Cleaner

# Objective: Use regex to clean and extract data from messy text.

# The Data
records = [
    "Name: Alice Johnson | Email: alice.j@gmail.com | Phone: (555) 123-4567 | Joined: 01/15/2023",
    "Name: Bob Smith | Email: bob_smith@yahoo.com | Phone: 555.987.6543 | Joined: 03-22-2023",
    "Name: Charlie Brown | Email: charlie@outlook.com | Phone: 555 111 2222 | Joined: 2023/07/01",
    "Name: Diana Prince | Email: diana.prince@company.co.uk | Phone: (555)444-3333 | Joined: 11/30/2023",
]

# Tasks - Write Python functions using re to:
# 1 extract_names(records) - Return a list of names
# 2 extract_emails(records) - Return a list of emails
# 3 normalize_phones(records) - Return all phone numbers in XXX-XXX-XXXX format
# 4 extract_dates(records) - Return all dates regardless of format

# Bonus: Write a function that parses each record into a dictionary: {"name": ..., "email": ..., "phone": ..., "joined": ...}

# Step 1: Extract names
import re
def extract_names(records):
    """Extract names from records."""
    return [re.search(r'Name:\s*([^|]+)', record).group(1).strip() for record in records]
names = extract_names(records)
print("=== Extracted Names ===")
print(names)  # ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'Diana Prince']

# Step 2: Extract emails
def extract_emails(records):
    """Extract emails from records."""
    return [re.search(r'Email:\s*([^|]+)', record).group(1).strip() for record in records]
emails = extract_emails(records)
print("=== Extracted Emails ===")
print(emails)  # ['alice.j@gmail.com', 'bob_smith@yahoo.com', 'charlie@outlook.com', 'diana.prince@company.co.uk']

# Step 3: Normalize phone numbers
def normalize_phones(records):
    """Extract and normalize phone numbers to XXX-XXX-XXXX format."""
    pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    def norm(s):
        digits = re.sub(r'\D', '', s)
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:10]}"

    return [norm(m.group()) for record in records for m in [re.search(pattern, record)] if m]
normalized_phones = normalize_phones(records)

print("=== Normalized Phones ===")
print(normalized_phones)  # ['Name: Alice Johnson | Email: alice.j@gmail    .com | Phone: 555-123-4567 | Joined: 01/15/2023', 'Name: Bob Smith | Email: bob_smith@yahoo.com | Phone: 555-987-6543 | Joined: 03-22-2023', 'Name: Charlie Brown | Email: charlie@outlook.com | Phone: 555-111-2222 | Joined: 2023/07/01', 'Name: Diana Prince | Email: diana.prince@company.co.uk | Phone: 555-444-3333 | Joined: 11/30/2023']

# Step 4: Extract dates
def extract_dates(records):
    """Extract dates from records regardless of format."""
    date_pattern = r'Joined:\s*(\d{2}[-/]\d{2}[-/]\d{4}|\d{4}[-/]\d{2}[-/]\d{2})'
    return [re.search(date_pattern, record).group(1) for record in records]
dates = extract_dates(records)
print("=== Extracted Dates ===")
print(dates)  # ['01/15/2023', '03-22-2023', '2023/07/01', '11/30/2023']

# Bonus: Parse each record into a dictionary
def parse_record(record):
    """Parse a record into a dictionary."""
    name = re.search(r'Name:\s*([^|]+)', record).group(1).strip()
    email = re.search(r'Email:\s*([^|]+)', record).group(1).strip()
    phone_match = re.search(r'Phone:\s*([^|]+)', record)
    phone = re.sub(r'\D', '', phone_match.group(1)) if phone_match else None
    phone = f"{phone[:3]}-{phone[3:6]}-{phone[6:10]}" if phone else None
    date_match = re.search(r'Joined:\s*(\d{2}[-/]\d{2}[-/]\d{4}|\d{4}[-/]\d{2}[-/]\d{2})', record)
    joined = date_match.group(1) if date_match else None
    return {"name": name, "email": email, "phone": phone, "joined": joined}
parsed_records = [parse_record(record) for record in records]

print("=== Parsed Records ===")
# Print each parsed record on its own line
for rec in parsed_records:
    print(rec)
# [{'name': 'Alice Johnson', 'email': 'alice.j@gmail.com', 'phone': '555-123-4567', 'joined': '01/15/2023'}, {'name': 'Bob Smith', 'email': 'bob_smith@yahoo.com', 'phone': '555-987-6543', 'joined': '03-22-2023'}, {'name': 'Charlie Brown', 'email': 'charlie@outlook.com', 'phone': '555-111-2222', 'joined': '2023/07/01'}, {'name': 'Diana Prince', 'email': 'diana.prince@company.co.uk', 'phone': '555-444-3333', 'joined': '11/30/2023'}]