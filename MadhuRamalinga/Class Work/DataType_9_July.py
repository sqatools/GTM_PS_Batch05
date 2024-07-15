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

a = 1787957983
print("Value of a is:",a, type(a))
print("_"*50)

############## Float Data Type ################
"""
Properties:
->  Float is immutable data type, once the value is assign you can not change it.
->  All positive and negative value can be consider as float
->  Float value only store pointer or decimal values.
->  There is no limit of value in the float. we can assign any long value in the float
"""
a = 152.026
print("Value of a is:",a, type(a))
print("_"*50)

########## complex data type ##############
"""
Properties:
-> complex number is combination of real and imaginary number.
-> complex data type is immutable data type.
-> complex number can contains positive and negative values.
"""

data = 5+10j
# r_data = data.real
print("Value of data is:", data)
# print("Value of real is:",r_data)
print("Value of real is:", data.real)
print("Value of imaginary is:",data.imag)

print("_"*50)

################### String Data Type ###############
"""
Properties :
->  String is immutable data type, once it is defined we can not change it.
->  string define with single/double/trip quotes.
->  String follows positive and negative indexing
"""
str1 = ''
str2 = "M"
str3 = "Good Morning"
str4 = 'My name is "Madhu"'
str5 = "My country is 'INDIA'"
str6 = """
Python Programming
"""

str7 = '''
1. Test 
2. data
'''

str8 = "Python " \
       "Programming " \

str9 = "1. Python\n" \
       "2. Programming \n" \

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

# Indexing in the string

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
print(str_b[1]) # e
print(str_b[-3]) # l

str_c = "Good Morning"
print("length of str_C :", len(str_c)) # 12

print(str_c[5])  # M
print(str_c[-7]) # M

str_d = "Hello"
str_e = "Good Morning"
str_f = str_d + " " + str_e
print("str_f :", str_f)  # Hello Good Morning

print("_"*50)

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
print(list2) # [3, 6, 7, 100]
print(list1[2]) # Hello

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