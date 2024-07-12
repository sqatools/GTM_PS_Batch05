a = 50
# a : variable
# = : assignment operator
# 50 : value
print(a)

address_a = id(a)
print("address of a :", address_a)
#_______________________________________________________________________
# if all variable have same value then their address location will be also same
p = 60
q = 60
r = 60

print ("address p:", id(p))
print ("address q:", id(q))
print ("address r:", id(r))
#________________________________________________________________________
#assign multiple variable and their different values at a time

x, y, z = 10 , 20 , 30
print ("Variable of x : ", x, "Variable of y :" ,y , "Variable of z:", z)

# OR
# In order to print a statement in one line
# end="" -- > it shows blank space
print ("variable of x:", x, end="/")
print ("variable of y:", y, end="/")
print ("variable of z:", z)

# OR
#  In order to print MULTILE  statement in MULTIPLE line
print ("variable of x:", x)
print ("variable of y:", y)
print ("variable of z:", z)
#_________________________________________________________________________
# assigning same value to multiple variable
a =b = c = 70
#OR
a,b,c = 70,70,70

print ("value of a : ", a)
print ("value of b : ", b)
print ("value of c : ", c)
 #OR
print ("Variable of a : ", a, "Variable of B :" ,b , "Variable of c:",c)
#_______________________________________________________________________
#Basics rules of variables
#1 space should not be there
# first name = 'rahul'
first_report = 'rahul'

#2 variable name cannot starts with numbers
#123abc = 82 (invalid)

#3 Variable names cannot have special character in it // undersore can be add '_'
#$%^dfg_123 = 895 (Invalid)

#4 there is not length limit for variable name
fjgvnerjgflkgjmfkgng1_87987645 = 234
print ("new value : ", fjgvnerjgflkgjmfkgng1_87987645)

#5 python is case sensitive (all variable as as different)
Name = 'mayuri'
name = "riya"
nAme = "vaishnavi"

print ("Name of candidate 1 :", Name, "Name of candidate 2 :", name ,"Name of candidate 3 :", nAme)
#OR
print (Name, name, nAme)
#___________________________________________________________________________
#multiline comment
"""
hjljl
hdxfghj
sdfgthjk
dfghjmklfcgvbhjnk
"""
#____________________________________________________________________________
"""
Mathematical Operator
+ : for addition
- : for subtraction
* : for multiplication
/ : divide with single slash
// : divide with double slash
!* : not equal Operator
% : Remainder Operator
** : Power operator
"""

#addition
# we cant add string with integers (20+python) --- not possible
a1 = 20
b1 = 6
c1 = 13
print ("addition of a1, b1 and c1 is ", a1+b1+c1)

w1 = "Hellow"
x1 = "Python"
y1 = "Learners"
print (w1 +" "+ x1 +" "+ y1)

#Subtraction
a2 = 20
b2 = 6
c2 = 13
print (a2 - b2 - c2 )

#Multiplication
#string with string multiplication not possible
a3 = 12
b3 = 6
c3 = 9
print ("Multiplication of above numbers are", a3*b3*c3)

#2
print ("hellow"*50)
print ("5"*8)
print ("_"*20)
print ("#"*8)
print (50 * " oops ")
print ("6"*8*8)

#_________________________________________________________________
#divide with single slash --- it will give values in decimal(15.6)
print ("Decimal value for 78/5 is ", 78/5)
print ("decimal value for float", 78.895/5)

#divide with double slash --- It will give values in whole number (15)
print ("Round of value for 78/5 is",  78//5)
print ("decimal value for float", 78.895//5)
#______________________________________________________________
#Remainder Operator
p1=13
q1= 5
print ("Reamainder valuefor p1 and q1 is", p1%q1)

#___________________________________________
#to check wheather number is divisivle by 2 mens its even or odd
# == 0 is use to check true or false

z5 = 5
print (z5%2 == 0)

y5 = 10
print (y5 % 2 == 0)
#_____________________________________________________
#Equal to operator
#use to compare twi different values
x=5
y=4
print (x==y) #false

x=70
y=80
z=80
print (y==z)
print(x==y)
print(x!=y)
#______________________________________________________

#power operator
print ("square of 5:", 5**2)
print ("cube of 5:", 5**3)
print ("cube of 7:", 7**3)
#______________________________________________________
# (a+b)^2 = a^2 + b^2+2ab  (prove this equation)
a=4
b=8
lhs = (a+b)**2
rhs = a**2 + b**2 + 2*a*b
print ("lhs value is",lhs )
print ("rhs value is",rhs )

print ("hence its proved that both values are same : ", lhs == rhs)

#_________________________________________________________

