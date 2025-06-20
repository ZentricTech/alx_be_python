class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year

        #print(f"{self.title} by {self.author} created.")
    
    def __del__(self):
        # Destructor prints a message when the object is deleted
        print(f"Deleting {self.title}")

    def __str__(self):
        # __str__ provides a user-friendly string representation
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # __repr__ provides a string that could recreate the Book instance
        return f"Book('{self.title}', '{self.author}', {self.year})"
        
