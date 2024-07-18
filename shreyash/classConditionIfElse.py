#write aprogram given value equal or not##
#a=40
#b=50
#print(a==b)

#a=50
#b=50
#print(a==b)

#a=50
#b=51
#if a==b:
#    print("variable A and B have equal value")
#else:
#    print("Variable A and B doesnt have equal value")

###check given number is even or not##
#num1 = 22
#print(num1%2==0)

#print("_"*40)
#num1 = 23
#print(1%2==0)
#if num1%2==0:
#    print("this is my even number")
#else:
#    print("this is my odd number")

##write a program if condition with and operator##

#a=50
#b=80
#c=70
#if b>a and b>c:
#    print("B has greater value")
#else:
#    print("B doesnt have greater value")

## OR condition program to check given number divisible 2 or 3##
#print("_"*40)
#num1 = 51
#if num1%2==0 or num1%3==0:
#    print("the number can divide by 2 or 3")
#else:
#    print("the number can not divide by 2 or 3")

##AND & OR condition####
##python program to check given number divisible by 2,3 or 5##

#var1=11
#if var1%2==0 or var1%3==0 and var1%5==0:
#    print("this number can divide by 2,3 and 5")
#else:
#    print("this numer can not divide by 2,3 and 5")
#eg2
#var1=50
#if var1%2==0 or var1%3==0 and var1%5==0:
#    print("this number can divide by 2,3 and 5")
#else:
#    print("this numer can not divide by 2,3 and 5")

##elif Condition##

###write a program to check greater value among different variables##
#p=50
#q=60
#r=70
#if p>q and p>r:
#    print("P is greater value: ",p)
#elif q>p and q>r:
#    print("q is greater value: ",q)
#elif r>p and r>q:
#    print("r is greater value: ",r)

##eg2 none of the variable has greater value
#p=60
#q=50
#r=60
#if p>q and p>r:
#    print("P is greater value: ",p)
#elif q>p and q>r:
#    print("q is greater value: ",q)
#elif r>p and r>q:
#    print("r is greater value: ",r)
#else:
#    print("none of the variable has greater value")

##write a program to demonstrate grading of students as per received marks##

#print("_"*50)

#marks=int (input("please enter the value"))
#print("marks", type(marks))

#if 30<marks<=40:
#    print("passed with 3rd grade")
#elif 40<marks<=50:
#    print("passed with 2nd grade")
#elif 50<marks<=60:
#    print("passed with 1st grade")
#elif 60<marks<=70:
#    print("passed with A grade")
#elif 70<marks<=80:
#    print("passed with A+ grade")
#elif 80<marks<=90:
#    print("passed with A++ grade")
#elif marks<=30:
#    print("You failed in the examiination")
#else:
#    print("Marks value should be between 0 to 100")

##Nested Condition##
#program on interview rounds of 3###

#round1= "Failed"
#round2= "Pass"
#round3= "Pass"
#if round1== "Pass":
#    print("cleared first round")
#else:
#    print("hard luck failed in 1st round")

##eg2##

#round1= "Pass"
#round2= "Pass"
#round3= "Failed"
#if round1== "Pass":
#    print("cleared first round")
#if round2== "Pass":
#    print("cleared second round")
#    if round3== "Pass":
#        print("congratulation you got placed")
#    else:
#        print("try next time")

##write a program with nested if condition if its even,check number divided by 4 or 8
# OR if the number odd then check the number can divided by 3 & 7

#num1=16
#num1%2==0
#print("this is even number")
#if num1%4==0 or num1%8==0:
#    print("this nummber is divisible by 4 or 8")
#else:
#    print("the number is odd")
#    if num1%3==0 or num1%7==0:
#        print("the number is divisible by 3 or 7")
#    else:
#        print("this is not divisible by 3 or 7")

##write a program to check given value is available in list or not

#list1= [4,6,8,2]
#val1=0
#if val1 in list1:
#    print("value is available in list1")
#else:
#    print("value is not available in list1")

##write a simple program with if condition with true or false##
#p= False
#if p:
#    print("p value is true")
#else:
#    print("p value is false")

##eg2#
#print("_"*40)
#p: "Hello"
#if p:
#    print("P is true value")
#else:
#    print("P is false value")

##write a program none condition with if##
#print("_"*50)
#q=[4,6,7,8]
#if q is not None:
#   print(q)
#else:
#    print("q has none value")

###############1 write a python program print all value which are divisible by and 3 and 5 from given list
#####
#list2 = [3, 9, 15, 30, 45, 16, 25]
#num =  int(input("Enter a number: "))

#if num%3 == 0  and num%5 == 0:

#    print("Given number can divide by both 3 and 5")
#else:
#    print("Given number can not divide by 3 and 5")

##Program to get all numbers divided by 3 between 1 to 30#

#for i in range(1,31):
# if i%3 == 0:
#    print(i,end=" ")

###Check a number is part of the Fibonacci series
#fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#num = int(input("Enter a number: "))
#if num in fib:

#    print("It is a part of the series")
#else:

#    print("It is not a part of the series")

#####Python program to check authentication with the given username and password
#name = input("Enter name:sunny ")
#password = input("Enter password:sunyy123 ")

#if name == password:

#    print("It is valid")
#else:

#    print("It is not valid")

###Check whether the given number is positive or not.
#num=int(input("enter a number "))
#if num>0:
#    print("true")
#else:
#    print("false" )

##Python program to print the largest number from two numbers##

#num1= int(input("enter first number "))
#num2= int(input("enter second number"))

#if num1>num2:
#    print("first number is greater")
#else:
#    print("second number is greater")

###Check whether the character is lowercase or not.###

char=input("enter the character: ")
if char is lower():
    print("true")
else:
    print("false")