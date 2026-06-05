# Regex in Python with the re Module

# Searching for Patterns
import re

text = "Call me at 555-123-4567 or email me at alice@example.com"

# re.search() — find the first match anywhere in the string
phone_match = re.search(r'\d{3}-\d{3}-\d{4}', text)
if phone_match:
    print(f"Found phone: {phone_match.group()}")  # 555-123-4567

# re.findall() — find ALL matches, returned as a list
all_numbers = re.findall(r'\d+', text)
print(f"All number sequences: {all_numbers}")  # ['555', '123', '4567']

# Important: Always use raw strings (r'...') for regex patterns. The r prefix tells Python not to interpret backslashes as escape characters.


# Extracting with Groups
text = "Order #12345 placed on 2025-01-15 for $49.99"

pattern = r'Order #(?P<order_id>\d+) placed on (?P<date>\d{4}-\d{2}-\d{2}) for \$(?P<price>[\d.]+)'

match = re.search(pattern, text)

if match:
    print(f"Order ID: {match.group('order_id')}")  # 12345
    print(f"Date: {match.group('date')}")           # 2025-01-15
    print(f"Price: {match.group('price')}")         # 49.99


# Replacing Text
messy_text = "Phone: (555) 123-4567 or 555.987.6543 or 555 111 2222"

def normalize_phone(match):
    """Strip all non-digits and reformat as XXX-XXX-XXXX."""
    digits = re.sub(r'\D', '', match.group())
    return f"{digits[:3]}-{digits[3:6]}-{digits[6:10]}"

clean = re.sub(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', normalize_phone, messy_text)
print(clean)  # Phone: 555-123-4567 or 555-987-6543 or 555-111-2222


# Validating Input
def is_valid_email(email):
    """Basic email validation with regex."""
    pattern = r'^[\w.+-]+@[\w-]+\.[\w.]+$'
    return bool(re.match(pattern, email))

print(is_valid_email("alice@example.com"))     # True
print(is_valid_email("bob.smith@company.co"))  # True
print(is_valid_email("not-an-email"))          # False
print(is_valid_email("@missing-user.com"))     # False

# Important caveat: Email validation by regex is notoriously difficult to get 100% right. In production, use a dedicated validation library (like Pydantic’s EmailStr in Module 5).


# Data Cleaning Example
addresses = [
    "123 Main St, Springfield, IL 62701",
    "456 Oak Ave., Chicago, IL 60601",
    "789 Pine Blvd, Peoria IL 61602",
]

# Extract zip codes
pattern = r'\b\d{5}\b'
zip_codes = [re.search(pattern, addr).group() for addr in addresses]
print(f"Zip codes: {zip_codes}")  # ['62701', '60601', '61602']

# Extract state abbreviations
pattern = r'\b([A-Z]{2})\s+\d{5}\b'
states = [re.search(pattern, addr).group(1) for addr in addresses]
print(f"States: {states}")  # ['IL', 'IL', 'IL']
