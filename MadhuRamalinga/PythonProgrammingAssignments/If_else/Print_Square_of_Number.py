# Python program to print the square of the number if it is divided by a certain number such as 10

num = int(input("Enter the number: "))
if num%10 == 0:
    print("Square of the number is: ", num**2)
else:
    print("the number is not divisible by 10")