#1.Python Program to add two integer values.
i=10
j=20
print("Add two Integer:",i+j)

#2.Python Program to subtract two integer values.
i=10
j=20
print("Subtract two Integer:",i-j)

#3.Python program to multiply two numbers.
i=10
j=20
print("Multiply two Numbers:",i*j)

#4.Python program to repeat a given string 5 times.
str1 = "SQATools"
print(5*"SQATools")

#5.Python program to get the Average of given numbers.
#Formula: sum of all the number/ total number
a = 40
b = 50
c = 30
d=int((a+b+c)/3)
print(d,type(d))

#6.Program to get the median of given numbers.
n=[45, 60, 61, 66, 70, 77, 80]
#n.sort()
m=(len(n))/2
print("Median:",n[int(m)])

#7.Python program to print the square and cube of a given number.
num1 = 9
print("Square Value of num1:",num1**2)
print("Square Value of num1:",num1**3)

#8.Python program to interchange values between variables.
a = 10
b = 20
a,b=b,a
print("a value is:",a)
print("b value is:",b)

#9.In this Python basic program, we will solve the Pythogorous theorem, which states,
# the square of the hypotenuse is equal to the sum of squares of other sides of the right triangle.
#a2 + b2 = c2
#a = side of a right triangle
#b = side of a right triangle
#c = hypotenuse

import math
a=5
b=7
Hypo=a**2+b**2
print(Hypo)
print("Square root of hypo:",math.sqrt(Hypo))

#10.Python program to solve the given math formula.
#Formula : (a + b)2 = a^2 + b^2 + 2ab

a=5
b=6
c=(a+b)**2
d=a**2+b**2+2*a*b
print("(a+b)2:",c)
print("a^2 + b^2 + 2ab:",d)

#11.Python program to solve the given math formula.
#Formula : (a – b)2 = a^2 + b^2 – 2ab
a=7
b=15
c=(a-b)**2
d=a**2+b**2-2*a*b
print("(a-b)2:",c)
print("a^2 + b^2 - 2ab:",d)

#12.Python program to solve the given math formula.
#Formula : a2 – b2 = (a-b)(a+b)

a=7
b=15
c=(a**2)
e=(b**2)
f=c-e
d=(a-b)*(a+b)
print("a2 – b2:",int(f))
print("(a-b)(a+b):",int(d))

#13.Python program to solve the given math formula.
#Formula : (a + b)3 = a3 + 3ab(a+b) + b3

a=8
b=16
c=(a+b)**3
e=(a**3)
f=(b**3)
d=e+3*a*b*(a+b)+f
print("(a + b)3:",int(c))
print("a3 + 3ab(a+b) + b3:",int(d))

#14.Python program to solve the given math formula.
#Formula : (a – b)3 = a3 – 3a^2b + 3ab^2 – b3

a=16
b=8
c=(a-b)**3
e=(a**3)
f=(b**3)
g=3*(a**2)*b
h=3*a*(b**2)
d= e- g+h -f
print("(a – b)3:",int(c))
print("a3 – 3a2b + 3ab2 – b3:",int(d))

#15.Python program to calculate the area of the square.
#Formula : area = a*a

#Sqr=int(input("Enter the area of Square:",))
a=12
print("Area of Square is:",a**2)

#16.Python program to print the current date
import datetime
date1=datetime.datetime.now()
print(date1.strftime("%Y %b %d"))

#17.Python program to calculate the area of a circle.
#Area of Circule is equal to Pir square

s=4
r=s**2
PI=3.14
print("Area of Circule is Equal to :",PI*r)

#18.Python program to calculate the area of a cube.
#Formula = 6*a*a

a=5
b=a**2
print("Area of Cube:",6*b)

#19.Python program to calculate the area of the cylinder.
#Formula = 2*PI*r*h + 2*PI*r*r

PI=3.14
r=5
h=4
PIrh=PI*r*h
PIr_2=PI*r*r
print("Area of the cylinder:",(2*PIrh)+(2*PIr_2))

#20.Python program to calculate simple interest.
#Formula = P+(P/r)*t
#P = Principle Amount
#r = Anual interest rate
#t = time

P=1000
r=20
t=3
PI=P+(P/r)*t
print("Simple Interest with Principle :",P+(P/r)*t)
print("Interest is:",PI-P)

#1
List1="Vinoth Vinoth Aksay Sugan Bala"
str2=List1.split(" ")
str1= len(str2)
length=0
for i in range(0,6):
    if len(str2)==5:
        length+=1
        print(str2)



