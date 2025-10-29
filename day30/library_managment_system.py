# Library Management System
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display_info(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")

class Library:
    def __init__(self):
        self.books =  []

    def add_book(self,title,author):
        new_book = Book(title,author)
        self.books.append(new_book)
        print(f"Book '{title}' added to the library")

    # View all boooks
    def view_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\n---Library Catalog ----")
            for book in self.books:
                book.display_info()

    # Borrow a book
    def borrow_book(self,title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                print(f"Book '{title}' has been borrowed.") 
                return 
            print(f"Book '{title}' is not available for borrowing.") 

    # Return a Book
    def return_book(self,title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                print(f"Book '{title}'  is not the library")
                return
        print(f"Book '{title} is not in the library.'")

#Main Program
Library = Library()

while True:
    print("\n--- Library Managment System ----")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5):").strip()

    if choice == "1":
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        Library.add_book(title,author)
    elif choice == "2":
        Library.view_books()
    elif choice == "3":
        title = input("Enter book title to borrow: ").strip()
        Library.borrow_book(title)
    else:
        print("Invalid choice. Please select a valid option (1-5).")            
                    
