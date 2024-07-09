####1) Python Program to add two integer values.
a=5
b=6
print("Add two integer :", a+b)      #11

print("-"*30)

######2) Python Program to subtract two integer values.
a=90
b=35
print("Subtract two integer values:", a-b) # 55

print("-"*30)

########3)Python program to multiply two numbers.
a=56
b=7
print("Multiply two number values:", a*b)  #392

print("-"*30)

#######4)Python program to repeat a given string 5 times.
print("Hi Python" " "*5) #Hi Python Hi Python Hi Python Hi Python Hi Python

str="Hi Python"
print(str*5)  #Hi PythonHi PythonHi PythonHi PythonHi Python

print("-"*30)

########5) Python program to get the Average of given numbers.
##Formula: sum of all the number/ total number
##Input:
a = 40
b = 50
c = 30
print("Avg no:", (a+b+c)/3)  #40.0

print("-"*30)

#####6) print the square and cube of a given number.
"""Input :
num1 = 9
Output :
Square = 81
Cube =   729"""
a=9
print("Square of a is :", a**2) #81
print("Cube of a is :", a**3) #729

print("-"*30)

#########7)Python program to interchange values between variables.
"""Input :
a = 10
b = 20
Output :
a = 20
b = 10"""
a=10
b=20
print("Values of a :", b)  #20
print("Value of b :", a)   #10

print("-"*30)

##########8)Python program to solve this Pythagorous theorem.
##Theorem : (a2 + b2 = c2)
a=3
b=4
c=5
LHS= (a**2 + b**2)
RHS= c**2
print("LHS :", LHS)  #25
print("RHS :", RHS)  #25

a=3
b=4
val=(a**2 + b**2)
print("Seconf method Pythagorous theorem", val)  #25

print("-"*30)

#####9) program to solve the given math formula.
##Formula : (a + b)2 = a^2 + b^2 + 2ab
x=8
y=9
RHS=x**2 + y**2 + 2*x*y
LHS=(x+y)**2
print("LHS", LHS)   #289
print("RHS", RHS)   #289
print(LHS == RHS)   #True

print("-"*30)

####10) Python program to solve the given math formula.
#Formula : (a – b)2 = a^2 + b^2 – 2ab

a=2
b=3
LHS= (a-b)**2
RHS= a**2 + b**2 -2*a*b
print("LHS", LHS)  #1
print("RHS", RHS)  #1
print(LHS == RHS)  #True

print("-"*30)

#####11)program to solve the given math formula.
#Formula : a2 – b2 = (a-b)(a+b)
a=8
b=6
LHS=(a**2)-(b**2)
RHS=(a-b)*(a+b)
print("LHS", LHS)  #28
print("RHS", RHS)  #28
print(LHS == RHS)  #True

print("-"*30)

####12)Python program to solve the given math formula.
#Formula : (a + b)3 = a3 + 3ab(a+b) + b3
a=2
b=3
LHS=(a+b)**3
RHS=a**3+3*a*b*(a+b)+b**3
print("LHS of cube :", LHS)  #125
print("RHS of cube:", RHS)   #125
print(LHS == RHS)            #True
print("Result of (a + b)3 =", RHS)    #125

print("-"*30)

####13) Python program to solve the given math formula.
#Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3
a=6
b=3
LHS=(a-b)**3
RHS=a**3 - 3*a**2*b + 3*a*b**2 -b**3
print("LHS of minus cube :", LHS)    #27
print("RHS of minus cube:", RHS)     #27
print(LHS == RHS)                    #True
print("Result of (a - b)3 =", RHS)   #27

print("-"*30)

####14)Python program to calculate the area of the square.
#Formula : area = a*a
a=6
area=a*a
print("area value:", area)    #36

print("-"*30)

###15) Python program to calculate the area of a circle.
"""Formula = PI*r*r
r = radius
PI = 3.14"""

r=6
PI=3.14
area=PI*r*r
print("Area of Circle:", area)    #113.03999999999999
print("Area of Circle2", PI*r*r)  #113.03999999999999

print("-"*30)

####16) Python program to calculate the area of a cube.
#Formula = 6*a*a

a=5
val=6*a*a
print("Area of a Cube :", 6*a*a)   #150
print("Area of a Cube2 :", val)    #150

print("-"*30)

#####17) Python program to calculate the area of the cylinder.
#Formula = 2*PI*r*h + 2*PI*r*r
r=5
h=7
PI=3.14
area=2*PI*r*h + 2*PI*r*r
print("area of the cylinder :", area)    #376.8

print("-"*30)

#####18) Python program to check whether the given number is an Armstrong number or not.
#Example: 153 = 1*1*1 + 5*5*5 + 3*3*3

LHS=153
RHS=1*1*1 + 5*5*5 +3*3*3
print("LHS :", LHS)    #153
print("RHS :", RHS)    #153
print(LHS == RHS)      #True

print("-"*30)

#####19) Python program to calculate simple interest.
"""Formula = P+(P/r)*t
P = Principle Amount
r = Anual interest rate
t = time"""
P=10000
r=12
t=3
Interest=P+(P/r)*t
print("interest: ", Interest)   #12500.0

print("-"*30)

###20) Python basic program to calculate compound interest
# using formula p*((1+r/100)**n).
p=10000
r=12
n=3
compound=p*((1+r/100)**n)
print("compound interest :", compound)   #14049.280000000004

print("-"*30)

####21) Python program to calculate the volume of a sphere.
"""Formula = (4/3*pi*r^2)
r = radius
pi = 3"""
PI=3.14
r=5
sphere=(4/3*PI*r**2)
print("volume of a sphere :", sphere)  #104.66666666666666

print("-"*30)








