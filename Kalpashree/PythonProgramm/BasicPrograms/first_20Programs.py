####Addition of two Integer####
a1 = 40
b1 = 50
print("Sum of two numbers:", a1+b1)


####Subtraction of two numbers####
p = 90
q = 40
print("Difference of two numbers:", p-q)

####Multiplication of two numbers####
x = 33
y = 15
print("product of two numbers:",x*y)

#####Repeat the given string#####
StrA = "AllisWell"
print("Repeat the string by multiplying",StrA*5)

####Average####
p1 = 3
q1 = 8
r1 = 6
print("Average of given number:",p1+q1+r1/3)

#### find the median ######
list = [30,40,70,10,80,60,20]
list.sort()
med= (len(list))/2
print("Median:",list[int(med)])

#### Square and Cube of a number#######
num1 = 5
print('Square:',num1**2)
print('Cube:',num1**3)

####interchange the value#####
J = 10
K = 20
J,K = K,J
print("Value of J:",J)
print("Value of K:",K)

####Pythagorous theorem###
#a^2+b^2=c^2
import math
p2 = 4 #one side value
q2 = 5 #other side value
hypo = p2**2+q2**2
print("hypotenious side:",math.sqrt(hypo))


####math Formula : (a + b)2 = a^2 + b^2 + 2ab####
a = 8
b = 3
result =a**2+b**2+2*a*b
print("(a + b)2:",result)

#### formaula (a – b)2 = a^2 + b^2 – 2ab ####
a2 = 5
b2 = 2
result2 =a2**2+b2**2-2*a2*b2
print("(a2 + b2)2:",result2)

####formaula  a2 – b2 = (a-b)(a+b)####
a1 = 5
b1 = 2
result1 =(a1-b1)*(a1+b1)
print("a2 – b2:",result1)

####formaula(a + b)3 = a3 + 3ab(a+b) + b3 ####
z= 5
y= 2
result3 =z**3+y**3+3*z*y*(z+y)
print("(z+y)3:", result3)


####formaula(a – b)3 = a3 – 3a2b + 3ab2 – b3 ####
z1=3
y1=2
result4 = z1**3-3*z1**2*y1+3*z1*y1**2-y1**3
print("((a – b)3:", result4)

#####Side of square####
side = 4 # can also use int(input("Enter the side of a square: "))
print("Area of sqaure: ",side**2)

######Radius of circle#####
radius = 3  # other method int(input("Enter radius of circle: "))
area = 3.14*radius*radius
print("Area of circle: ",area)

####area of a cube####
side = int(input("Enter side of a cube: "))
area1=6*side*side
print("Area of cube: ",area1)

####area of the cylinder####
r = int(input("Enter radius of cylinder: "))
h = int(input("Enter height of cylinder: "))
area2= 2*3.14*r*h+2*3.14*r*r
print("Area of cylinder: ",area2)

####check given number is an Armstrong number or noT####
num = 370
sum = 0
n1 = len(str(num))
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** n1
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

#####simple interests####
p = 15000
r = 10
t = 5
amount = p+(p/r)*t
print("Amount payable: ",amount)

###Print current date ####
print("_"*50)
import datetime
date = datetime.datetime.now()
print (date.strftime (" %Y %b %d "))


###calculate days between 2 dates using datetime library ####
print("_"*50)
from datetime import date
date_1 = date(2024, 7, 5)
date_2 = date(2024, 7, 22)
result = (date_2 - date_1).days
print ("Number of Days between the given Dates are: ", result, "days")