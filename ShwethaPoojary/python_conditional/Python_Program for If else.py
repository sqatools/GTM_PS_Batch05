############################# If else Programm ##############
print("_"*50)
# 1) Python program to check given number is divided by 3 or not.
#num=int(input("Enter a Number:"))
num=3
if num%3==0:
    print("Given Number divided by 3")
else:
    print("Given number not divided by 3")

#Enter a Number:15
#Given Number divided by 3

#Enter a Number:19
#Given number not divided by 3
print("_"*50)

# 2)If else program to assign grades as per total marks.
# marks < 40: Fail
# marks 40 – 50: grade C
# marks 50 – 60: grade B
# marks 60 – 70: grade A
# marks 70 – 80: grade A+
# marks 80 – 90: grade A++
# marks 90 – 100: grade Excellent
# marks > 100: Invalid marks

#marks=int(input("Enter marks:"))
marks=5
if marks<=40:
    print("Fail")
elif 40< marks <=50:
    print("Grade C")
elif 50 < marks <=60:
    print("Grade B")
elif 60 < marks <=70:
    print("Grade A")
elif 70 < marks <=80:
    print("Grade A+")
elif 80 < marks <=90:
    print("Grade A++")
elif 90< marks <=100:
    print("Excellent")
elif marks >100:
    print("Invalid marks")
else:
    print("Invalid")

#Enter marks: 45
#Grade C
#Enter marks:30
#Fail
#Enter marks:68
#Grade A

print("_"*50)
###3) Python program to check the given number divided by 3 and 5.

#num=int(input("Enter a number:"))
num=3
if num%3==0 and num%5==0:
    print("Number divided by 3 and 5")
else:
    print("number not divided by 3 and 5")

''' Enter a number:15
Number divided by 3 and 5
Enter a number:35
number not divided by 3 and 5
Enter a number:33
number not divided by 3 and 5
'''
print("-"*50)

# 4)Python program to print the square of the number if it is divided by 11
#num=int(input("Enter a number:"))
num=11
if num%11==0:
    print("Square of number:", num**2)
else:
    print("Number not divided by 11")

'''Enter a number:22
Square of number: 484
Enter a number:44
Square of number: 1936
'''
print("-"*50)
##5)Python program to check given number is odd or even
#num=int(input("Enter a number:"))
num=8
'''
if num%2==0:
    print("Given number is Even")
elif num%2!=0:
    print("Given number is odd")
else:
    print("Invlid")
    '''
if num%2==0:
    print("Given number is Even")
else:
    print("Given number is odd")

'''
Enter a number:4
Given number is Even
Enter a number:17
Given number is odd
'''

print("-"*50)

##6)Python program to check authentication with the given username and password

#name=input("Enter your Name:")
#password=input("Enter Password:")
name="S"
password="S"
if name==password:
    print("Valid")
else:
    print("Invalid")

'''
Enter your Name:shwetha
Enter Password:shwetha
Valid
Enter your Name:ShwetHa
Enter Password:Shwetha
Invalid
'''
print("-"*50)

###7)Python program to validate user_id in the list of user_ids.
list_ID=[1,4,6,7,9,14,37]
#id=int(input("Enter your ID: "))
id=8
if id in list_ID:
    print("Valid")
else:
    print("Invalid")

'''Enter your ID: 7
    Valid
    Enter your ID: 40
Invalid
    '''
print("-"*50)

###8)Python program to print a square or cube if the given number is divided by 2 or 3 respectively.
#num1=int(input("Enter a number: "))
num1=5
if num1%2==0 or num1%3==0:
    print("Sqaue or Cube of number:", num1**2, num1**3)
else:
    print("Invalid")
'''
Enter a number: 15
Sqaue or Cube of number: 225 3375
Enter a number: 7
Invalid
'''
print("_"*50)


###9)Python program to describe the interview process
#round1 = input("Enter Round 1 result:")
#round2 = input("Enter Round 2 result:")
#round3 = input("Enter Round 3 result:")
round1 = "Passed"
round2 = "Passed"
round3 = "Passed"
if round1 == "Passed":
    print("1st Round clear")
    if round2 == "Passed":
        print("2nd Round Clear")
        if round3 == "Passed":
            print("Congratulations")
        else:
            print("Fail in 3rd Round")
    else:
        print("Fail in 2nd Round")
else:
    print("Fail in 1st Round")

'''Enter Round 1 result:Passed
Enter Round 2 result:Passed
Enter Round 3 result:Passed
1st Round clear
2nd Round Clear
Congratulations

Enter Round 1 result:Passed
Enter Round 2 result:fail
Enter Round 3 result:Passed
1st Round clear
Fail in 2nd Round

1st Round clear
2nd Round Clear
Fail in 3rd Round

Enter Round 1 result:fail
Enter Round 2 result:passed
Enter Round 3 result:passed
Fail in 1st Round
'''
print("-"*50)
###10)Python program to determine whether a given number is available in the list of numbers or not.
List_number = [1,4,7,9,40,37,24,78]
#num2 = int(input("Enter a number: "))
num2=9
if num2 in List_number:
    print("Input number is available in list")
else:
    print("Given number is not in list")
'''
Enter a number: 7
Input number is available in list
Enter a number: 5
Given number is not in list

'''

print("-"*50)

######11)Python program to find the largest number among three numbers
#num1 = int(input("enter 1st number:"))
#num2 = int(input("enter 2nd number:"))
#num3 = int(input("enter 3rd number:"))

num1=6
num2=5
num3=7
if num1>num2 and num1>num3:
    print("Greatest number is Num1:", num1)
elif num2>num1 and num2>num3:
    print("Greatest number is Num2:", num2)
elif num3>num1 and num3>num2:
    print("Greatest number is Num3:", num3)
else:
    print("Invalid")

'''enter 1st number:4
enter 2nd number:6
enter 3rd number:3
Greatest number is Num2: 6

enter 1st number:7
enter 2nd number:5
enter 3rd number:3
Greatest number is Num1: 7

enter 1st number:2
enter 2nd number:5
enter 3rd number:9
Greatest number is Num3: 9
'''

print("-"*50)

#####12) Python program to check any person eligible to vote or not
#age > 18+ : eligible
#age < 18: not eligible

#age=int(input("Enter age: "))
age=30
if age >= 18:
    print("Eligible for Vote")
elif age < 18:
    print("Not Eligible")
else:
    print("Enter valid number")

'''Enter age: 20
Eligible for Vote

Enter age: 18
Eligible for Vote

Enter age: 17
Not Eligible
'''

print("-"*50)

###13) Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.
#Input = Enter marks: 45
#Output = Pass
#marks=int(input("Enter marks: "))
marks=90
if marks > 35:
    print("Pass")
else:
    print("Fail")

'''
Enter marks: 45
Pass
Enter marks: 30
Fail
'''

print("-"*50)

##14) Python program to check whether the given number is positive or not.
#Input = 20
#Output = True

#num = int(input("Enter a number: "))
num=9
if num > 0:
    print("True")
else:
    print("False")

'''
Enter a number: 5
True
Enter a number: -5
False
'''
print("-"*50)

##15) Python program to check whether the given number is negative or not.
#Input = -45
#Output = True

#num = int(input("Enter a number: "))
num=6
if num < 0:
    print("True")
else:
    print("False")

'''
Enter a number: 5
False
Enter a number: -8
True
'''
print("-"*50)

###16)Python program to check whether the given number is positive or negative and even or odd.
#Input = 26
#Output = The given number is positive and even

#num = int(input("Enter a number :"))
num=9
if num > 0:
    if num%2 ==0:
        print("The given number is Positive and Even")
    else:
        print("The given number is Positive and Odd")
else:
      if num%2 ==0:
        print("The given number is Negative and Even")
      else:
        print("the given number is Negative and Odd")


'''
Enter a number :6
The given number is Positive and Even
Enter a number :-7
the given number is Negative and Odd
Enter a number :9
The given number is Positive and Odd
Enter a number :-10
The given number is Negative and Even
'''

print("-"*50)

###17)Python program to print the largest number from two numbers.
#Input:25, 63
#Output = 63
#Num1 = int(input("Enter a number Num1: "))
#Num2 = int(input("Enter a number Num2: "))
Num1=67
Num2=45
if Num1 > Num2:
    print("Largest number is Num1:", Num1)
else:
    print("Largest number is Num2:", Num2)

'''Enter a number Num1: 23
Enter a number Num2: 654
Largest number is Num2: 654

Enter a number Num1: 234
Enter a number Num2: 32
Largest number is Num1: 234
'''

print("-"*50)

##18)Python program to check whether the given number is an integer or not.
#Input = 54
#Output = True
num = 25.6
if type(num) == int:
    print("True")
else:
    print("False")

'''
45
True
25.6
False
'''

print("-"*50)
##19)Python program to check whether the given number is float or not.
#Input = 12
#Output = True
num = 25
if type(num) == float:
    print("True")
else:
    print("False")

'''
25.74
True
25
False
'''
print("-"*50)
##20)Python program to check whether the given input is a string or not.
#Input = ‘sqatools’
#Output = True

a1=234
if type(a1) == str:
     print("True")
else:
    print("False")

'''
"AAAAA"
True
234
False
'''


