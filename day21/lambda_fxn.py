# def addition(a,b):
#     return a + b

# addition(2,3)

addition = lambda a,b:a+b
type(addition)
print("The addition",addition(2,3))


# def even(num):
#     if num % 2 == 0:
#         return True
# even(24)    

even= lambda num:num%2==0
type(even)
print("The even:",even)

addition  = lambda x,y,z:x+y+z
print("The addition of x,y and z:",addition(1,2,3))

