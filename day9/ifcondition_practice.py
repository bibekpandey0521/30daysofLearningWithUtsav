# Q1
number = int(input("Enter a number:"))

if number > 5:
    print("The number is greater than 5.")
elif number == 5: 
    print("The number is equal to 5.")   
else:
    print("The number is less than 5.")    

# Q2    
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))

if a > 5 and  b < 15:
    print("Both conditions are true.")
else:
    print("At least one condition is false")

# Number Comparison Tool

# Step 1: Get user input for two numbers
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

# Step 2 : Compare the numbers and print the result
print("\n--Comparsion Results ------")
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 > num2 :
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num1} is less than {num2}")    

# Step 3 : Check if any number is zero
if num1 == 0 or num2 == 0:
    print("\nAt least one number is zero.") 
else:
    print("\nBoth numbers are non-zero")       