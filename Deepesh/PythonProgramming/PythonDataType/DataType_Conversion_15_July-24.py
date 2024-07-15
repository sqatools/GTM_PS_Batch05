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
#################################### Tuple ########################

## tuple -> int # conversion is not possible
## tuple  -> float # conversion is not possible
## tuple -> string ####
tup2 = (4, 6, 7, 8)
str2 = str(tup2)
print(str2, type(str2), str2[1])
# (4, 6, 7, 8) <class 'str'> 4

#### tuple -> list ###
print("_"*50)
tup2 = (3, 5, 7, 2)
list2 = list(tup2)
print(list2, type(list2), list2[1])
# [3, 5, 7, 2] <class 'list'> 5

### tuple ->  dict ## conversion is not possible
### tuple -> set ###
print("_"*50)
tup3 = (4, 6, 7, 2, 4, 7, 6)
set3 = set(tup3)
print(set3, type(set3))
# {2, 4, 6, 7} <class 'set'>


### tuple -> boolean ###
print("_"*50)
tup4 = tuple()
bool4 = bool(tup4)
print(bool4, type(bool4))
# False <class 'bool'>

tup5 = (4, 6, 7)
bool5 = bool(tup5)
print(bool5, type(bool5))
# True <class 'bool'>

############################ Dictionary #############

##dict -> int ## conversion is not possible
## dict -> float ### conversion is not possible
## dict -> string ###
print("_"*40)
dict1 = {'a': 123, 'b': 456, 'c': 678}
print(dict1)
str1 = str(dict1)
print(str1, type(str1), str1[0], str1[2])
# {'a': 123, 'b': 456, 'c': 678} <class 'str'> { a

### dict -> list ###
print("_"*40)
dict_a= {'a': 123, 'b': 456, 'c': 678}
list_a = list(dict_a)
print(list_a, type(list_a))
# ['a', 'b', 'c'] <class 'list'>

#### Dict -> tuple ###
print("_"*40)
dict_b= {'a': 123, 'b': 456, 'c': 678}
tup_b  = tuple(dict_b)
print(tup_b, type(tup_b))
# ('a', 'b', 'c') <class 'tuple'>


### dict -> set ###
print("_"*40)
dict_c= {'a': 123, 'b': 456, 'c': 678}
set_c = set(dict_c)
print(set_c, type(set_c))
# {'b', 'a', 'c'} <class 'set'>

### dict -> bool ###
print("_"*50)
dict_d = {}
bool_d = bool(dict_d)
print(bool_d, type(bool_d))
# False <class 'bool'>


dict_e = {'Name' : 'Rahul'}
bool_e = bool(dict_e)
print(bool_e, type(bool_e))
# True <class 'bool'>


##################### Set ################

## set -> int ### conversion is not possible
## set -> float ### conversion is not possible
## set -> string ###
print("_"*40)
set_a = {4, 6, 2, 7, 1, 'a', 'b'}
str_a = str(set_a)
print(str_a, type(str_a), str_a[1])
# {1, 2, 4, 6, 7, 'a', 'b'} <class 'str'> 1

### set -> list ###
print("_"*50)
set_b = {5, 7, 3, 2, 5}
list_b = list(set_b)
print(list_b, type(list_b), list_b[0])
# [2, 3, 5, 7] <class 'list'> 2

### set -> tuple ###
print("_"*50)
set_c = {5, 7, 3, 2, 5, 7, 2}
tup_c = tuple(set_c)
print(tup_c, type(tup_c), tup_c[0])
# (2, 3, 5, 7) <class 'tuple'> 2

### set -> dict ## conversion is not possible

### set -> bool ###
set_d = set()
bool_d = bool(set_d)
print(bool_d, type(bool_d))
# False <class 'bool'>

set_e = {5, 7, 8}
bool_e = bool(set_e)
print(bool_e, type(bool_e))
# True <class 'bool'>

