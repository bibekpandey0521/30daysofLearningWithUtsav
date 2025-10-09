def function_name():
    #code block insde the function
    print("Hello from the function")
function_name()    

def greet():
    print("Hello,welcome to Python!")

greet()

def greet(name):
    print(f"Hello, {name}! welcome to Python!")
greet('John')    


def add(a,b):
    print(f"The sum is :  {a+b}")
add(3,4)

def multiply(a,b):
    return a*b
result = multiply(5,4)
print("The result is: ",result)