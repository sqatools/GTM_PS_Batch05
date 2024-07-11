a = 50
# a : variable
# = : assignment operator
# 50 : value
print(a)

address_a = id(a)
print("address of a :", address_a)
#____________________________________________________________________________
# if all variable have same value then their address location will be also same
p = 60
q = 60
r = 60

print ("address p:", id(p))
print ("address q:", id(q))
print ("address r:", id(r))
#____________________________________________________________________________
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
#____________________________________________________________________________
#multiline comment
"""
hjljl
hdxfghj
sdfgthjk
dfghjmklfcgvbhjnk
"""
#_____________________________________________________________________________
"""
Mathematical Operator
+ : for addition
- : for substraction
* : for multiplication
/ : divide with single slash
// : divide with double slash
!* : not equal Operator
% : Remainder Operator

"""


