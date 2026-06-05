# Build a Library Catalog

# Objective: Design and implement a class hierarchy for managing a collection of books.

#1. Book class

    # Attributes: title, author, year, checked_out (boolean, starts False)
    # Methods: check_out(), return_book(), __repr__ (shows title, author, and status)
    # Validation: year must be a positive integer
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Year must be a positive integer")
        self.year = year
        
        self.checked_out = False

    def check_out(self):
        if self.checked_out:
            print(f"'{self.title}' is already checked out.")
        else:
            self.checked_out = True
            print(f"You have checked out '{self.title}'.")

    def return_book(self):
        if not self.checked_out:
            print(f"'{self.title}' was not checked out.")
        else:
            self.checked_out = False
            print(f"You have returned '{self.title}'.")

    def __repr__(self):
        status = "Checked Out" if self.checked_out else "Available"
        return f"'{self.title}' by {self.author} ({self.year}) - {status}"

#2. EBook class (inherits from Book)
    # Additional attribute: file_size_mb
    # Override __repr__ to include file size
    # Override check_out() , ebooks can be checked out by multiple people simultaneously (hint: use a counter instead of a boolean)
class EBook(Book):
    def __init__(self, title, author, year, file_size_mb):
        super().__init__(title, author, year)
        
        if not isinstance(file_size_mb, (int, float)) or file_size_mb <= 0:
            raise ValueError("File size must be a positive number")
        self.file_size_mb = file_size_mb
        
        self.checkout_count = 0  # Counter for how many times the ebook is checked out

    def check_out(self):
        self.checkout_count += 1
        print(f"You have checked out '{self.title}'. Total checkouts: {self.checkout_count}")

    def return_book(self):
        if self.checkout_count == 0:
            print(f"'{self.title}' was not checked out.")
        else:
            self.checkout_count -= 1
            print(f"You have returned '{self.title}'. Remaining checkouts: {self.checkout_count}")

    def __repr__(self):
        base_repr = super().__repr__()
        return f"{base_repr} [File Size: {self.file_size_mb} MB]"

#3 Catalog class
    # Methods: add_book(book), search_by_author(author), search_by_title(keyword), get_available(), summary()
    # search_by_title should find books where the keyword appears anywhere in the title (case-insensitive)
class Catalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise ValueError("Only Book or EBook instances can be added to the catalog")
        self.books.append(book)

    def search_by_author(self, author):
        return [book for book in self.books if book.author.lower() == author.lower()]

    def search_by_title(self, keyword):
        return [book for book in self.books if keyword.lower() in book.title.lower()]

    def get_available(self):
        return [book for book in self.books if not book.checked_out and (not isinstance(book, EBook) or book.checkout_count == 0)]

    def summary(self):
        print(f"Catalog Summary: {len(self.books)} books total")
        for book in self.books:
            print(f"  {book}")

# Test the code
catalog = Catalog()
catalog.add_book(Book("Python Crash Course", "Eric Matthes", 2019))
catalog.add_book(Book("Clean Code", "Robert Martin", 2008))
catalog.add_book(EBook("AI Engineering", "Chip Huyen", 2025, 15.2))

# Search
results = catalog.search_by_title("python")
print(results)  # Should find "Python Crash Course"

# Check out
catalog.books[0].check_out()
available = catalog.get_available()
print(f"Available: {len(available)} books")

catalog.summary()