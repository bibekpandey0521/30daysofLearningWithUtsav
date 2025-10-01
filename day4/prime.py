# To Take input form the user
num = int(input("Enter a number:"))
# check for factors
if num == 1:
    print((num, ' is not a prime number!'))
elif num > 1 :
    for i in range(2,num):
        if(num % i) == 0 :
            print(num, " is not a prime number")
            print(i, "items ", num//i ,"is ",num)
            break
        else:
            print(num,'is a prime number')
            break
# if input number is less than 
# or equal to 1, it is not prime

else:
    print(num, 'is not a prime number')

