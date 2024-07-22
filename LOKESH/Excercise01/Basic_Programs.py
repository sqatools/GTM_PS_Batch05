##1). Python Program to add two integer values##
A = 30
B = 40
C = (A+B)
print("Addision of A and B:", A+B)
print(C)

##2). Python Program to subtract two integer values.
print('_' * 80)
D = 12
E = 15
print ("Substraction of E and D:",E-D)

##3). Python program to multiply two numbers.
print('_' * 80)
F = 25
G = 30
print ("multiplication of F and G:",F*G)

##4). Python program to repeat a given string 5 times.
print('_' * 80)
str1 = "SQATools"
print("Repeating string for 5 times:", "SQATools || " * 5 )

##5). Python program to get the Average of given numbers.
print('_' * 80)
a = 40
b = 50
c = 30
print("Average: ",(a+b+c)/3)

##6)Python program to get the median of given numbers.
##Note: all the numbers should be arranged in ascending order
##Formula : (n+1)/2
##n = Number of values
print('_' * 80)

list1 = [45, 60, 61, 66, 70, 77, 80]
# x = len(list1) - > python len function Returns the number of items in a list.
# print(x)
list1.sort()
a = (len(list1))/2
print("Median: ",list1[int(a)])

##7).  Python program to print the square and cube of a given number.
print('_' * 80)
num1 = 9

print("num1 square: ", num1 ** 2)
print("num1 square: ", num1 ** 3)

##8). Python program to interchange values between variables.
print('_' * 80)
a = 10
b = 20

a,b = b,a
print(a,b)

##9). Python program to solve the given math formula.
##Formula : a2 – b2 = (a-b)(a+b)
print('_' * 80)
a = 3
b = 2

result = (a+b) * (a-b)
print ("num1 square: ", result)

##10). Python program to calculate the area of a cube.
##Formula = 6*a*a
print('_' * 80)

# side = int(input("Enter side of a cube: "))
# area = 6*side*side
#
# print("Area of cube: ",area)

##11). Python program to print the current date in the given format
##Output: 2023 Jan 05
##Note: Use the DateTime library
print('_' * 80)

import datetime
date = datetime.datetime.now()

print(date.strftime(" %Y %b %d "))

##12). Python program to calculate days between 2 dates.
##Input date : (2023, 1, 5) (2023, 1, 22)
##Output: 17 days
print('_' * 80)

from datetime import date
date_1 = (2023, 1, 5)
date_2 = (2023, 1, 22)
date1 = date(date_1[0], date_1[1], date_1[2])
date2 = date(date_2[0], date_2[1], date_2[2])

result = (date2 - date1).days

print ("Number of Days between the given Dates are: ", result, "days")


##13). Python program to reverse a given number.
# print('_' * 80)
#
# num = int(input("Enter a number: "))
# reverse = str(num)
# print("Reverse: ",reverse[::-1])


##14). Program to generate random numbers.
print('_' * 80)

import random

for i in range(5):
    print(random.random())

##15).Python program to get the current date using datetime.
print('_' * 80)

import datetime
dt = datetime.datetime.now()

print("Current Date: ",dt)

##16).Program to find the square root of a number.
print('_' * 80)

import math
num1 = 9

print(math.sqrt(num1))














