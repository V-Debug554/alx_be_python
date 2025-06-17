# Script to solidify understanding of basic OOP concepts in Python by implementing a system that tracks books in a library.

# Define the Book class
class Book:
    def __init__(self, title, author):
        self.title = title                     # Public attribute for the book title
        self.author = author                   # Public attribute for the author
        self._is_checked_out = False           # Private attribute to track if book is checked out (default: available)

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True        # Mark book as checked out
            return True                        # Indicate success
        else:
            return False                       # Cannot check out a book that’s already checked out

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False       # Mark book as returned (available)
            return True                        # Indicate success
        else:
            return False                       # Cannot return a book that wasn’t checked out

    def is_available(self):
        return not self._is_checked_out        # Returns True if book is available (not checked out)

    def __str__(self):
        return f"{self.title} by {self.author}"  # Nicely formats the book for printing

# Define the Library class
class Library:
    def __init__(self):
        self._books = []                        # Private list to store book instances

    def add_book(self, book):
        # Adds a book to the collection. Must be a Book instance.
        if isinstance(book, Book):
            self._books.append(book)            # Correctly adds the book
        else:
            raise ValueError("Only Book instances can be added to the library.")

    def check_out_book(self, title):
        # Looks for a book by title and checks it out if available
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()                # Use the Book's check_out method
                return True                     # Successful checkout
        return False                            # Book not found or already checked out

    def return_book(self, title):
        # Looks for a checked-out book by title and returns it
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()              # Use the Book's return_book method
                return True                     # Successfully returned
        return False                            # Book not found or wasn’t checked out

    def list_available_books(self):
        # List only books that are not checked out
        for book in self._books:
            if book.is_available():
                print(f"  {book}")              # Indented format to match expected output
