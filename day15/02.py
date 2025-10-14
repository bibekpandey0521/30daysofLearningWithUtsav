# try:
    # Code that might raise an exception
# except ExceptionType:
    # Code to handle the exception    
# else:
    # Execute if no exception occurs 

# finally:
    # Always execute, even if an exception occurs 
  
try:
    num = int(input("Enter a number:"))
    result = 10 / num
    print("Result: ",result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
else:
    print("No exception occured. Result: ", result)
finally:
    print("Finally block executed.")    