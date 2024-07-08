p, q, r = 30, 40, 50
print("p :", p, "q :", q, "r :", r)


a = b = c = 50
print(a, b, c)

#x, y, z, = 30
#print("x :",x, "y:", y, "z:", z)
# TypeError: cannot unpack non-iterable int object


# 123abc = 100 # invalid
# abc_123, abc123, ab_c123
# xyz$pqr = 4000 : invalid
# print(xyz)


"""
Math operator
+ : plus operator
- : subtraction operator
* : multiple operator
/ : divide with single slace
// : divide with double slace
== : equal to operator
!= : not equal operator
% : remainder operator
** : power operator
"""

###### Addition of values ###

var1 = 50
var2 = 60
print("addition of number :", var1+var2) # 110

str1= "Hello"
str2 = "Good Morning"
print("add two word :", str1 +" "+str2)  # Hello Good Morning

#########
# assign empty value
str3 = None
print(str3)

####### multiplication #############
v1= 50
v2 = 6
print("multiplication :", v1*v2) #  300

str1 = "Python"
print("multiply number with string :", str1*5)
# PythonPythonPythonPythonPython

print("5"*50)
# 55555555555555555555555555555555555555555555555555
print("_"*50)
#__________________________________________________
print("$"*5*5)
# $$$$$$$$$$$$$$$$$$$$$$$$$
print(15*"&")
# &&&&&&&&&&&&&&&

#print("Hello"*"Python")
# can't multiply sequence by non-int of type 'str'

##########subtraction ###########
print("_"*50)

a1 = 60
b1 = 30
print("subtraction 1:", a1-b1) # 30
print("subtraction 2:", b1-a1) # -30

########## Division ###########
print("_"*50)

a2 = 50.45
b2 = 7

print("divide with single / :", a2/b2) # 8.333333333333334
print("divide with single // :", a2//b2) # 8

print("")
################ remainder #########
print("_"*50)
p1 = 13
p2 = 5

print("remainder value :", p1%p2)

num1 = 16
remainder = num1%2
print(remainder == 0)

###########equal to operator ########
print("_"*50)
x = 50
y = 60
z = 50
# compare both variable have same value
print(x == y) # False
print(x == z) # True
print(x != y) # True


########## power operator #########

print("square of 4:", 4**2)
print("cube of 3:", 3**3)
print("square of 5:", 5**2)
print("cube of 5:", 5**3)

##################### solve the below quadratic equation #########
# (a+b)^2  = a^2 + b^2 + 2ab
a = 5
b = 6
lhs = (a+b)**2
rhs = a**2 + b**2 + 2*a*b
print("LHS :", lhs)
print("RHS :", rhs)
print(lhs == rhs)
