class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False


    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

# Create an object
book1 = Book("1984","George Orwell")
book1.display_info()

class BankAccount:
    def __init__(self,owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

account = BankAccount("John Doe",1000)
account.deposit(500) 