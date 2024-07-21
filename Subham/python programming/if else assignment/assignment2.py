#program to check given number is divided by 3 or not
num=int(input("please enter a number:"))
if num%3==0:
    print("number divisble by 3")
else:
    print("number not divisble by 3")
#Enter a Number:15
#Given Number divided by 3

#Enter a Number:19
#Given number not divided by 3

print("_"*50)

#If else program to get all the numbers divided by 3 from 1 to 30
for i in range (1,31):
    if i%3==0:
        print (i)

print ("_"*50)


# If else program to assign grades as per total marks.
#marks > 40: Fail
#marks 40 – 50: grade C
#marks 50 – 60: grade B
#marks 60 – 70: grade A
#marks 70 – 80: grade A+
#marks 80 – 90: grade A++
#marks 90 – 100: grade Excellent
#marks > 100: Invalid marks


marks =int(input("please enter marks:"))
print(marks,type(marks))
if marks<=40:
    print("fail")
elif 40< marks <=50:
    print("passed with C garde")
elif 50< marks <=60:
    print("passed with B garde")
elif 60< marks <=70:
    print("passed with A garde")
elif 70< marks <=80:
    print("passed with A+ garde")
elif 80< marks <=90:
    print("passed with A++ garde")
elif 90< marks <=100:
    print("passed with excellent garde")
elif marks >=100:
    print ("invalid marks")

print("_"*50)

#program to check the given number divided by 3 and 5.

num = int(input("enter a number:"))
if num%3==0 and num%5==0:
    print("divided 3 and 5")
else:
    print("invalid")

print("_" * 50)


#Python program to print the square of the number if it is divided by 11.

num = int(input("enter a number:"))
if num%11==0:
    print(num**2)
else:
    print("number not divided by 11")

print("_" * 50)

#Python program to check given number is a prime number or not
num = int(input("enter a number:"))
if num<1:
    for i in range(1,num+1):
        if(num%1)==0:
            count=count+1
    if count%2==0:
        print("number is prime")
    else:
        print("number is not prime")

print("_" * 50)

#Python program to check given number is odd or even

num = int(input("enter a number:"))

if num%2==0:
    print("its a even number")
else:
    print("its a odd number")

print("_" * 50)

#Python program to check a given number is part of the Fibonacci series from 1 to 10

fib=[0,1,2,3,5,8,13,21,34,55,89]
num = int(input("enter a number:"))

if num in fib:
    print("it is fibonacci number")
else:
    print("is is not a fibonacci number")


print("_" * 50)

#Python program to check authentication with the given username and password

name=input("enter user name")
password=input("enter user name")

if name== password:
    print("it is valid")
else:
    print("it not a valid")

print("_" * 50)


#Python program to validate user_id in the list of user_ids.



list_id = [1,2,3,4,5,6,7]

id =7

if id in list_id:
    print("its a valid id")

else:
    print("its not a valid id")

print("_" * 50)

#Python program to print a square or cube if the given number is divided by 2 or 3 respectively

num = 5
if num**2==0 and num**3==0:
    print("cube squre and cube:",num**2,num**3)
else:
    ("its invalid")


print("_" * 50)


#Python program to describe the interview process.


tech_round1="passed"
tech_round2="passed"
hr_round3="passed"

if tech_round1 == "passed":
    print("tech_round1 clear")
    if tech_round2 == "passed":
        print("tech_round2 clear")
        if hr_round3 == "passed":
            print("hr_round3 cong")
        else:
            print("fail in hr_round3")
    else:
        print("fail in tech_round2")
 else:
        print("fail in tech_round1")


print("_" * 50)


#Python program to determine whether a given number is available in the list of numbers or not.

list[1,2,3,4,5,6,7]

num2=5

if num2 in list :
    print("input number avilable in list")

else:
    print("given number not in list")

print("_" * 50)


#Python program to find the largest number among three numbers.
num1=5
num2=6
num3=7
if num1>num2 and num1>num2:
    print("greatest number number is:", num1)
elif num2>num1 and num2>num3:
    print("greatest number number is:", num2)
elif num3>num1 and num3>num2:
    print("greatest number number is:", num3)
else:
    print("invalid")

print("_" * 50)

# Python program to check any person eligible to vote or not
#age > 18+ : eligible
#age < 18: not eligible

age=58

if age<18:
    print("eligible for vote")
elif age>18:
    print("not eligible for vote")
else:
    print("enter a valid age")




















































































































































