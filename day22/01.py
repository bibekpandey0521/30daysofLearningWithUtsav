def square(x):
    return x*x
square(4)


numbers = [1,2,3,4,5,6,7,8]
# map fxn
map(square,numbers)
list(map(square,numbers))

## Lambda function with map
numbers = [1,2,3,4,5,6,7,8]
list(map(lambda x:x*x,numbers))


## MAP multiple multiple iterables
numbers1 = [1,2,3]
numbers2 = [4,5,6]

added_numbers = list(map(lambda x,y:x+y,numbers1,numbers2))
print(added_numbers)