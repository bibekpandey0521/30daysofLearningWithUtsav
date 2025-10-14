try:
    num = int(input("Enter a number:"))
    result = 10 / num
except (ZeroDivisionError,ValueError):
    print("Error: Division by zero or Invalid Input.")        

def withdraw(amount):
    if amount < 0 :
        raise ValueError("Invalid withdrawal amount - Amount cannot be negative")
    print(f"You have withdrawn ${amount}")

try:
    withdraw(-50)
except ValueError as e:
    print(e)    