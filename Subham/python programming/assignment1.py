# Python Program to add two integer values.
a=6
b=5
print(a+b)

#Python Program to subtract two integer values.
s=77
p=50
print(s-p)

#Python program to multiply two numbers.
z=55
x=40
print(z*x)

#Python program to repeat a given string 5 times.
s=("subham")
print(s*5)

#Python program to get the Average of given numbers.
a=48
b=50
c=77
print('average:',(a+b+c)//3)

#program to get the median of given numbers.
list= [20,30,50,70,80,90,10]
list.sort()
s = (len(list))/2
print("Median: ",list[int(s)])

#program to print the square and cube of a given number
#square
print("sqaure of 75:",75**2)
#cube
print("cube of 99:",99**3)

#interchange values between variables.
s=88
p=55
s,p = p,s
print("s:",s)
print("p:",p)

#solve this Pythagorous theorem
#(a2 + b2 = c2)
import math
s1=50
p1=40
hypo = s1**2+p1**2
print("Hypotenious s: ",math.sqrt(hypo))

#math formula
#(a + b)2 = a^2 + b^2 + 2ab
a=77
b=84
lhs=(a+b)**2
rhs=a**2+b**2+2*a*b
print("lhs:",lhs)
print("rhs:",rhs)
print(lhs==rhs)

#math formula
#(a - b)2 = a^2 + b^2 -2ab
a=45
b=56
lhs=(a-b)**2
rhs=a**2+b**2-2*a*b
print("lhs:",lhs)
print("rhs:",rhs)
print(lhs==rhs)

#a2 – b2 = (a-b)(a+b)
a=85
b=75
lhs=(a**2-b**2)
rhs=(a-b)*(a+b)
print("lhs:",lhs)
print("rhs:",rhs)
print(lhs==rhs)

#math formula
#(a + b)3 = a3 + 3ab(a+b) + b3
a=5
b=6
lhs=a+b**3
rhs=a**3+3*a*b*a+b+b**3
print("lhs:",lhs)
print("rhs:",rhs)
print(lhs==rhs)

































































