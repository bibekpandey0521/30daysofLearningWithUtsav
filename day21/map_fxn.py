numbers = [1, 2, 3, 4, 5, 6]

def square(number):
    return number ** 2

# Correct usage: just printing the result
print(f"The square is {square(2)}")

# Squaring all numbers in the list using map and lambda
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)
