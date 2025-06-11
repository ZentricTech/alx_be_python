class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        """Initialize the book with a title, author, and availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Initially, the book is available

    def check_out(self):
        """Mark the book as checked out (unavailable)."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # Book is already checked out

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # Book was not checked out
    
    def is_available(self):
        """Return whether the book is available for checkout."""
        return not self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """A class representing a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize an empty library."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book from the library."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False  # Book not found or not available

    def return_book(self, title):
        """Return a book to the library."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False  # Book not found or wasn't checked out

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [str(book) for book in self._books if book.is_available()]
        if available_books:
            print("\n".join(available_books))
        else:
            print("No books available.")
