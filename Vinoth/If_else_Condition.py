
#1.Python program to check given number is divided by 3 or not.
num = 30
if num%3 == 0:
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3")

#2). If else program to get all the numbers divided by 3 from 1 to 30.
for i in range(1,31):
    if i%3 == 0:
        print(i,end=" ")

# 3). If else program to assign grades as per total marks.
# marks > 40: Fail
# marks 40 – 50: grade C
# marks 50 – 60: grade B
# marks 60 – 70: grade A
# marks 70 – 80: grade A+
# marks 80 – 90: grade A++
# marks 90 – 100: grade Excellent
# marks > 100: Invalid marks

marks = 78
if marks<40:
    print("Fail")
elif marks>=40 and marks>=50:
    print("Grade C")
elif marks>50 and marks<=60:
    print("Grade B")
elif marks>60 and marks<=70:
    print("Grade A")
elif marks>70 and marks<=80:
    print("Grade A+")
elif marks>80 and marks<=90:
    print("Grade A++")
elif marks>90 and marks<=100:
    print("Excellent")
else:
    print("Invalid marks")

# 4).Python program to check the given number divided by 3 and 5.
num =15

if num%3 == 0  and num%5 == 0:
    print("Given number can divide by both 3 and 5")
else:
    print("Given number can not divide by 3 and 5")


# 5).Python program to print the square of the number if it is divided by 11.
num = 121
if num%11 == 0:
    print(num**2)
else:
    print("Number is not divisible by 11")


# 6).Python program to check given number is a prime number or not.
num =7
count = 0

for i in range(2,num):

    if num%i == 0:
        count += 1

if count > 0:
    print("It is not a prime number")
else:
    print("It is a prime number")


# 7).Python program to check given number is odd or even.

num=77
if num%2 == 0:
    print("It is an even number")
else:
    print("It is an odd number")

# 8).Python program to check a given number is part of the Fibonacci series from 1 to 10.
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

num =5
if num in fib:
    print("It is a part of the series")
else:
    print("It is not a part of the series")

# 9).Python program to check authentication with the given username and password.
name = "Vinoth"
password = 1234
if name == password:
    print("It is valid")
else:
    print("It is not valid")


# 10). Python program to validate user_id in the list of user_ids.
id_list = [1,2,3,5,6,7,8]

id_ =7
if id_ in id_list:
    print("Valid ID")
else:
    print("Invalid ID")


# 11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.
num = 14

if num%2 == 0:
    print("Sqaure: ",num**2)
elif num%3 == 0:
    print("Cube: ",num**3)


# 12). Python program to describe the interview process.
round1 = "passed"
round2 = "passed"

if round1 == "passed":
    print("Congrats your 1st round is clear")
    if round2 == "passed":
        print("Congrats 2nd round is clear, you are placed")
    else:
        print("Failed in 2nd round, please try next time")
else:
    print("Failed in 1st round, please try next time")


# 13). Python program to determine whether a given number is available in the list of numbers or not.
list1 = [22,33,49,34,65,67,12,25]
num = 22

if num in list1:
    print(f"{num} is available in the list")
else:
    print(f"{num} is not available in the list")


# 14). Python program to find the largest number among three numbers.
num1 = 12
num2 = 14
num3 = 16

if num1>num2:
    if num1>num3:
        print(f"{num1} is the greatest")
    else:
        print(f"{num3} is the greatest")
else:
    if num2>num3:
        print(f"{num2} is the greatest")
    else:
        print(f"{num3} is the greatest")


# 15). Python program to check any person eligible to vote or not
# age > 18+ : eligible
# age < 18: not eligible

age=19
if age >= 18:
    print("You are eligible")
else:
    print("You are not eligible")


# 16). Python program to check whether any given number is a palindrome.
# Input: 121
# Output: palindrome
num1 = 121
num2 = str(num1)

if num1 == int(num2[::-1]):
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")


# 17). Python program to check if any given string is palindrome or not.
# Input: ‘jaj’
# output = palindrome
str1 = 'jaj'
str2 = str1[::-1]

if str1 == str2:
    print("It is a palindrome string")
else:
    print("It is not a palindrome string")


# 18). Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.
# Input = Enter marks: 45
# Output = Pass
marks = 47

if marks>=45:
    print("Pass")
else:
    print("Fail")


# 19). Python program to check whether the given number is positive or not.
# Input = 20
# Output = True
num=79
if num>0:
    print("True")
else:
    print("False")

# 20). Python program to check whether the given number is negative or not.
# Input = -45
# Output = True
num = -56

if num<0:
    print("True")
else:
    print("False")

