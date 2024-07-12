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
####################### String ########################

## string -> int ###

# we can not convert string into int if it contains character/word
"""
str1 = "Hello"
num1 = int(str1)
print(num1)
# invalid literal for int() with base 10: 'Hello'
"""

# We can convert string into int if it contains only numbers
str2 = "34567"
num2 = int(str2)
print(num2, type(num2), num2*2)
# 34567 <class 'int'> 69134


######str -> float ######
print("_"*40)
"""
str_a = "Python"
num_a = float(str_a)
print(num_a)
# ValueError: could not convert string to float: 'Python'
"""

# If string contains only pointer values then we can convert string into float.
str_b = "55.678"
num_b = float(str_b)
print(num_b, type(num_b),  num_b*10)
# 55.678 <class 'float'> 556.78


#######string -> list ##########
print("_"*40)
str_c = "Programming"
list_c = list(str_c)
print(list_c, type(list_c))
# ['P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g'] <class 'list'>
print(list_c[0]) # P

####### string -> tuple ######
print("_"*40)
str_d = "Python"
tup_d = tuple(str_d)
print(tup_d, type(tup_d))
# ('P', 'y', 't', 'h', 'o', 'n') <class 'tuple'>
print(tup_d[-1]) # n

###### string -> dictionary ######

print("_"*40)
"""
# convertion is not possible
str_e = "Hello"
dict_e = dict(str_e)
print(dict_e)
# ValueError: dictionary update sequence element #0 has length 1; 2 is required
"""

import json
str_f = '{"Name":"Rahul", "email": "rahul@gmail.com", "city" : "Pune"}'
print(str_f, type(str_f))
# {"Name":"Rahul", "email": "rahul@gmail.com", "city" : "Pune"} <class 'str'>
data_dict = json.loads(str_f)
print(data_dict, type(data_dict))
# {'Name': 'Rahul', 'email': 'rahul@gmail.com', 'city': 'Pune'} <class 'dict'>
print(data_dict['Name']) # Rahul
print(data_dict['email']) # rahul@gmail.com

### string -> set #########
print("_"*40)
str_t = "Python Programming"
set_t = set(str_t)
print(set_t, type(set_t))
# {'i', 'o', 'y', ' ', 't', 'a', 'h', 'g', 'n', 'm', 'r', 'P'} <class 'set'>

#### string ->  boolean ####
print("_"*40)

str_e = ""
bool_e = bool(str_e)
print(bool_e)  # False

str_g = "Hello"
bool_g = bool(str_g)
print(bool_g) # True


############################ List ##############################

### list -> int #### conversion is not possible
### list -> float ## conversion is not possible
### list -> string ##
print("_"*50)
list_a = [2, 3, 4, 'P', 'Q', 'R']
str_a = str(list_a)
print(str_a, type(str_a))
# [2, 3, 4, 'P', 'Q', 'R'] <class 'str'>
print(str_a[0], str_a[1], str_a[-1])
# [ 2 ]


### list -> tuple ####
print("_"*40)
list_b = [40, 50, 60, 70]
tup_b = tuple(list_b)
print(tup_b, type(tup_b), tup_b[0])
# (40, 50, 60, 70) <class 'tuple'> 40


#### list -> dict ### conversion is not possible
"""
print("_"*50)
list_c = [4, 6, 7, 2]
dict_c = dict(list_c)
print(dict_c)
# TypeError: cannot convert dictionary update sequence element #0 to a sequence
"""

list1 = ['Hello', 'Python', 'Programming']
list2 = [3, 6, 7]
result = dict(zip(list1, list2))
print(result, type(result))
# {'p': 3, 'q': 6, 'r': 7} <class 'dict'>
# {'Hello': 3, 'Python': 6, 'Programming': 7} <class 'dict'>



### list -> set ###
list_h = [2, 3, 4, 2, 4, 5, 7, 3]
set_h = set(list_h)
print(set_h) # {2, 3, 4, 5, 7}


### list -> boolean ###
print("_"*40)
list_k = []
bool_k = bool(list_k)
print(bool_k) # False

list_r = [3, 5, 6]
bool_r = bool(list_r)
print(bool_r) # True


