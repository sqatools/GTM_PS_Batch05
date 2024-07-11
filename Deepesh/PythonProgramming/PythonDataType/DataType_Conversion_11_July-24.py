"""
Python Data Type

1. Numbers
    i).   Integer
    ii).  Float
    iii). Complex Number

2. Sequential
    i). String
    ii). List
    iii). Tuple

3. Dictionary
4. Set
5. Boolean
"""

############### Integer ###########
## int -> float
num1 = 35
print(num1, type(num1)) # 35 <class 'int'>
num2 = float(num1)
print(num2, type(num2)) # 35.0 <class 'float'>

print(float(num1))

## int -> string
print("_"*50)
var_a = 567
str_a = str(var_a)
print(str_a, type(str_a), str_a[0])
#print(var_a[0])

## int ->  list # conversion is not possible
"""
var_b = 676
list_b = list(var_b)
print(list_b)
# TypeError: 'int' object is not iterable
"""

### int -> tuple  # conversion is not possible
### int - dictionary # conversion is not possible
### int -> set # conversion is not possible
### int -> boolean
print("_"*50)
num1 = 0
bool_val = bool(num1)
print(bool_val)  # False

num2 = -123
bool_val2 = bool(num2)
print(bool_val2)  # True

################# Float ##################
print("_"*50)
###float - int

var_c = 66.45
var_d = int(var_c)
print(var_d, type(var_d))
# 66 <class 'int'>

### float -> string
var_f = 55.67
str_f = str(var_f)
print(str_f, type(str_f), str_f[3])
# 55.67 <class 'str'> 6

### float -> list # conversion is not possible
### float -> tuple # conversion is not possible
### float -> dict # conversion is not possible
### float -> set # conversion is not possible
### float -> boolean
var_h = 0.0
var_b = bool(var_h)
print(var_b) # False

var_j = 33.45
var_k = bool(var_j)
print(var_k) # True
