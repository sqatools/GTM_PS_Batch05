a = 50
# a : variable
# = : assignment operator
# 50 : value
print(a)

address_a = id(a)
print("address of a :", address_a)

# if all variable have same value, then their address location is also same
p = 60
q = 60
r = 60
add_p = id(p)
print("address p :",add_p) # 140733310390552
print("address q :",id(q)) # 140733310390552
print("address r :",id(r)) # 140733310390552

# assign multiple variable and different at a time

x, y, z = 30, 40, 50
print("value of x :", x)
print("value of y :", y)
print("value of z :", z)

print(" value x:", x, end="||")
print(" value y:", y, end="||")
print(" value z:", z)
# value x: 30|| value y: 40|| value z: 50||

# Assign same value to multiple variables

a = b = c = 70
print("value of a :", a) # 70
print("value of b :", b) # 70
print("value of c :", c) # 70

######  Rule to define the variables #######
# 1. there should not be space in variable name
# first name = 'rahul' # invalid variable
first_name = 'rahul'  # correct name

# 2. Variable name can not start with number
# 123_abc = 500 : invalid variable
abc_123 = 500 # valid name

# 3.  Variable name can not contains special character

# var_1_%_xyz = 600  : invalid name-> special character is not allowed
# var_1_@#$%^&* = 800 : invalid
_var_xyz_pqr = 700   # valid name

# 4. there is no length limit to defined variable
python_programming_variable_xyz_pqr = 8989080 # valid name
var1= "Hello" # valid name

# 5. Python variable is case sensitive

name = "Mohit"
Name = "Rahul"
NamE = "Aman"
namE = "John"
NAME = "Python"
print(name, Name, NamE, namE, NAME)
# Mohit Rahul Aman John Python

list1 = [45, 60, 61, 66, 70, 77, 80]
list1.sort()
a = (len(list1))/2
print("Median: ",list1[int(a)])
