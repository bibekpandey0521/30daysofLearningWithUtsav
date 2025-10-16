# 01
squares = [x**2 for x in range(10)]
print(squares)

# 02
numbers = [1,2,3,4,5]
doubled = [x * 2 for x in numbers]
print(doubled)

# 03
numbers = [1,2,3,4,5,6,7]
evens = [x for x in numbers if x % 2 == 0]
print(evens)

# 04 
names = ["Alice","Bob","Charlie","David"]
uppercase_names = [name.upper() for name in names]
print(uppercase_names)

# 05
names  = ["Alice","Bob","Charlie","David"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

# 06
numbers = [1,2,3,4,5,6]
labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(labels)



