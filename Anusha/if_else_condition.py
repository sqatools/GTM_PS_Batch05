
#Syntax of If else condition
"""
if condition:
    code
else:
    code

"""
a = 50
b = 51
print(a == b)
#1
if a == b:
    print("variable A and B have equal value")
else:
    print("Variable A and B does not have equal value")

#2
    x=3
    y=6
    print(x==y)
    print("-"*50)
    if x==y:
        print("x and y are equal")
    else:
        print("x and y are not equal")

#3  check given number is even or not
print("-"*50)
numb=24
print(numb%2==0)
if numb%2==0:
    print("Given number is even")
else:
    print("given number is odd")


#4 Program to check if a number is divisible by 3
print("-"*50)
number=15
if number % 3==0:
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3")

#5 Program to get all numbers divided by 3 between 1 to 40
print("-"*50)
for i in range (1,31):
    if i % 3 == 0:
        print(i,end = " ")

#6 write a if condition program with and operator
print("-"*50)
a = 50
b = 80
c = 70
if b > a and c > a:
    print("B is greater")
else:
    print("B is not greater")

# 7 write a python program to check given number is divisible by 2 or 3.
print("-"*50)
numb=15
if numb % 2 == 0 and numb % 3 == 0:
    print("Dvisible by 2")
else:
    print("Divisible by 3")


# 8  python program to check given number is divisible by 2 ,3 or 5
print("-"*50)
numb=25
if numb % 2 == 0 or numb % 3 == 0 and numb % 5 == 0:
    print(" Given number is divisible by 2,3,5")
else:
    print(" Given number is not divisible by 2,3,5")


#9 Python program to check number is divided by 3 and 5
print("-"*50)
numb = 15
if numb % 3 == 0 and numb % 5 == 0:
    print("Given number is divisible by 3 and 5")
else:
    print("Given number is not divisible by 3 and 5")

#10 Python program to print the square of the number
print("-"*50)
numb = 4
if numb % 3 == 0 and numb % 5 == 0:
    print("Given number is divisible by 3 and 5")
else:
    print("Given number is not divisible by 3 and 5")