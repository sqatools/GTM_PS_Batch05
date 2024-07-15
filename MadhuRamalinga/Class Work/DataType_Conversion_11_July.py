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
a1 = 5
print(a1) # 5
# print(float(a1)) # 5.0
b1 = float(a1)
print(b1) # 5.0

print("_"*50)

## int -> string
a2 = 105
print(a2) # 105
# b2 = str(a2)
# print(b2[0], type(b2))
print((str(a2))[2])

print("_"*50)

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
a3 = 0
bool_val1 = bool(a3)
print(bool_val1)  # False

b3 = -123
bool_val2 = bool(b3)
print(bool_val2)  # True

print("_"*50)

################# Float ##################

###float - int

a4 = 10.85
d4 = int(a4)
print(d4, type(d4)) # 10 <class 'int'>

### float -> string
a5 = 108.56
b5 = str(a5)
print(b5, type(b5), b5[3])
print(b5, b5[-1], type(b5))

### float -> list # conversion is not possible
### float -> tuple # conversion is not possible
### float -> dict # conversion is not possible
### float -> set # conversion is not possible

### float -> boolean
a5 = 0.0
b5 = bool(a5)
print(b5) # False

a6 = 58.45
b6 = bool(a6)
print(b6) # True




