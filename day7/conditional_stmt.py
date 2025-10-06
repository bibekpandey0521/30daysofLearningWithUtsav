## if statement
age = int(input("Enter your age:"))

if age>=18:
    print("You are allowed to vote in the elections")
elif age<13:
    print("You are a child")
elif age<18:
    print("You are teenager")    
else:
    print("You are an adult")


##nested conditional Statements 

num = int(input("Enter the number:"))

if num >=0:
    print("The number is positive")
    if num %2==0:
        print("The number is even")    
    else:
        print("The number is odd")    
else:
    print("The number is  zero or negative")        