# def fuunction_name():
#     # Code
#     return value

def add(a,b) :
    return a + b

result = add(10,20)
print(result)

def rectangle_area(width,height):
    return width * height

area = rectangle_area(10,20)
print(area)

def math_operations(a,b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    return addition,subtraction,multiplication,division

add,subtract,multiply, divide = math_operations(10,5)
print(f"The addition of 10 + 5 is  {add}")
print(f"The subtraction of 10 - 5 is {subtract}")
print(f"The  multiplication of 10 * 5 is {multiply}")
print(f"The division of 10 - 5 is {divide}")