# Function to add two numbers
def add(x,y):
    return x+y

# Function to subtract two numbers
def subtract(x,y):
    return x - y

# Function to mulitply two numbers
def mulitply(x,y):
    return x*y

# Function to divide two numbers
def divide (x,y):
    if y == 0:
        return "Error! Division by zero not allowed."
    else :
        return x/y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        #Take input from the user
        choice = input("Enter choices (1/2/3/4):")

        #Check if the input is one of the four
        if choice in ['1','2','3','4']:
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter second number:"))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1,num2)}")
            if choice == '2':
                print(f"{num1} - {num2} = {subtract(num1,num2)}")
            if choice == '3':
                print(f"{num1} * {num2} = {mulitply(num1,num2)}")
            if choice == '4':
                print(f"{num1} / {num2} = {divide(num1,num2)}") 

        # Option to exit the loop                  
        next_calculation  = input("Do you want to perform another calculation? (yes/no):")
        if next_calculation.lower() != 'yes':
            break

    print("Exiting Calculator!")

# Call the calculator function        
calculator()