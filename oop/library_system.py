class Book:
    def __init__(self, title, author):
        # Base class initialization
        self.title = title
        self.author = author

    def __str__(self):
        # String representation for Book
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        # Call the parent class constructor to initialize title and author
        super().__init__(title, author)
        # Initialize the specific attribute for EBook
        self.file_size = file_size

    def __str__(self):
        # String representation for EBook, includes file size
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Call the parent class constructor to initialize title and author
        super().__init__(title, author)
        # Initialize the specific attribute for PrintBook
        self.page_count = page_count

    def __str__(self):
        # String representation for PrintBook, includes page count
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        # Initialize the library with an empty list of books
        self.books = []

    def add_book(self, book):
        # Add a book (or ebook or printbook) to the library
        self.books.append(book)

    def list_books(self):
        # Print the details of all books in the library
        for book in self.books:
            print(book)
