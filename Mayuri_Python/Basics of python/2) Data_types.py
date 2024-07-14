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

################# Integer Data Type ###########
"""
Properties:
->  Integer is immutable data type, once the value is assign you can not change it
->  All positive and negative value can be consider as integer
->  There is no limit of value in the integer. we can assign any long value in the integer
->  Only whole number will be consider as integer.
"""
var1 = 100
print(type(var1))  # <class 'int'>
var2 = 5563456435634564356345654363456
print(var2, type(var2))
# 5563456435634564356345654363456 <class 'int'>

var3 = -6545645654
print(var3, type(var3))  # -6545645654 <class 'int'>

############## Float Data Type ################
"""
Properties:
->  Float is immutable data type, once the value is assign you can not change it.
->  All positive and negative value can be consider as float
->  Float value only store pointer or decimal values.
->  There is no limit of value in the float. we can assign any long value in the float
"""

var_a = 55.45
var_b = -660.30
var_c = 546456456.464564523252435
var_d = 0.0
print("var_a :", var_a, type(var_a))  # 55.45 <class 'float'>
print("var_b :", var_b, type(var_b))  # -660.3 <class 'float'>
print("var_c :", var_c, type(var_c))  # 546456456.4645646 <class 'float'>
print("var_d :", var_d, type(var_d))  # 0.0 <class 'float'>


########## complex data type ##############
"""
Properties:
-> complex number is combination of real and imaginary number.
-> complex data type is immutable data type.
-> complex number can contains positive and negative values.
"""

print("_"*50)
#  x+yj
data = 10+20j
print(data, type(data))

print("real value :", data.real, type(data.real))
print("imaginary value :", data.imag, type(data.imag))

data2 = 40 + 50j

data3 = data + data2
print("data3 :", data3)


################### String Data Type ###############
print("_"*50)
"""
Properties :
->  String is immutable data type, once it is defined we can not change it.
->  string define with single/double/trip quotes.
->  String follows positive and negative indexing
"""
str1 = ''
str2 = "H"
str3 = "Good Morning"
str4 = 'My name is "Rahul"'
str5 = "My country name is 'INIDA'"
str6 = """
Test data generation refers to the 
process of creating and maintaining
values for testing with the intention 
of using it for testing purposes. 
It consists of creating synthetic
"""

str7 = '''
1. Test data generation 
2. refers to the process 
3. of creating and maintaining 
4. values for testing with the 
5. intention of using it for 
'''

str8 = "Test data generation refers to the " \
       "process of creating and maintaining values " \
       "for testing with the intention of using it for " \
       "testing purposes. It consists of creating synthetic " \
       "or representative data to validate the functionality, performance,"

str9 = "1. Apple\n" \
       "2. Banana \n" \
       "3. Mango\n" \
       "4. Pinnapple \n" \
       "5. Lichi"


print("str1 :", str1, ":", type(str1))
print("+"*50)
print("str2 :", str2, ":", type(str2))
print("+"*50)
print("str3 :", str3, ":", type(str3))
print("+"*50)
print("str4 :", str4, ":", type(str4))
print("+"*50)
print("str5 :", str5, ":", type(str5))
print("+"*50)
print("str6 :", str6, ":", type(str6))
print("+"*50)
print("str7 :", str7, ":", type(str7))
print("+"*50)
print("str8 :", str8, ":", type(str8))
print("+"*50)
print("str9 :", str9, ":", type(str9))
print("+"*50)


# Indexin in the string

str_a = "Python"

"""
  0   1   2   3   4   5    +ve indexing
  P   Y   T   H   O   N
 -6   -5  -4  -3  -2  -1   -ve indexing 
"""

print(str_a[0])  # P
print(str_a[-6]) # P

print(str_a[4])  # o

str_b = "Hello"
print(str_b[1])
print(str_b[-3])

str_c = "Good Morning"
print("length of str_C :", len(str_c))

print(str_c[5])  # M
print(str_c[-7]) # M

str_d = "Hello"
str_e = "Good Morning"
str_f = str_d + " " + str_e
print("str_f :", str_f)  # Hello Good Morning

#################### List Data Type ###############
print("_"*50)
"""
Properties :

->  list is mutable data type, once it is defined we can change it.
->  List can contains all type of data, int, float, str, list, tuple, dict, set, boolean.
->  List values are comma separated.
->  List follows positive and negative indexing as like string.
"""

list1 = [3, 33.56, 'Hello', [4, 6, 7], (3, 8, 2), {'a' : 123, 'b' : 345},
         {4, 6, 8, 2}, True, None]

print("list1 :", list1, type(list1))  # <class 'list'>

list2 = [3, 6, 7]
list2.append(100)
print(list2)
print(list1[2])

import keyword
print(keyword.kwlist)
"""
['False', 'None', 'True', 'and', 'as', 'assert', 
'async', 'await', 'break', 'class', 'continue', 
'def', 'del', 'elif', 'else', 'except', 'finally', 
'for', 'from', 'global', 'if', 'import', 'in', 'is', 
'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
'return', 'try', 'while', 'with', 'yield']
"""
#        0     1   2           3
list2 = ['a', 'b', [4, 7, 8], 'c']
#        -4   -3   -2          -1

print(list2[1])  # b

print(list2[2])  # [4, 7, 8]

print(list2[2][1])  # 7















