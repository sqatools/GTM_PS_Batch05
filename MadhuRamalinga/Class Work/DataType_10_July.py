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

################# Tuple data type ###########
"""
Properties :
-> Tuple is immutable data type, once it is defined we can not modify.
-> Tuple can store all type of data, int, float, string, list, tuple, dict, set, boolean
-> Tuple follows the positive and negative indexing as like string and list.
-> Tuple defined with round bracket.
-> We should use tuple where the data is fixed, which is not going to change once it is 
   defined. e.g  months in year, days in week, number of alphabets.
-> Tuple is faster than list in terms of performance.
"""

tup = (4, 4.5, 'hello', [4, 6, 8], (4, 1, 3), {'Name': 'Alex'},
        {5, 7}, True)  # <class 'tuple'>

print(tup, type(tup))

tup2 = (4, 6, 7, (3, 9, 2), 'a', 'b')

print(tup2[3])  # (3, 9, 2)

print(tup2[3][2])  # 2

print("_"*50)

############## Dictionary data type ##########
"""
Properties :

-> dictionary is mutable data type, we can update the data whenever we want.
-> dictionary store data in key value pair, each data can be identify by unique key.
-> dictionary does not allow duplicate key, the keys are always unique.
-> All immutable data type can be key in the dictionary, int, float, string, tuple, boolean.
-> All type of data can be value in dictionary, int, float, string, list, dictionary, set, boolean
-> Dictionary value can be duplicate in the data set.
-> Dictionary does not follow any indexing.
"""

dict1 = {'a': 123, 'b': 456}

print(dict1['a'])  # 123

# add new key and value in dict
dict1['c'] = 500
dict1['d'] = 123

print(dict1, type(dict1))
# {'a': 123, 'b': 456, 'c': 500, 'd': 123} <class 'dict'>

# update existing key value
dict1['a'] = 555
print(dict1)

# add mutable data type as key
# dict1[[1, 2, 3]] = 888
# print(dict1)
# TypeError: unshakable type: 'list'
dict2 = {}
dict2[123] = [3, 5, 6]
dict2[45.55] = {'a': 234, 'b': 678}
dict2[(7, 1, 3)] = {3, 7, 1, 5}
dict2[True] = 1000

print("dict2 :", dict2) # dict2 : {123: [3, 5, 6], 45.55: {'a': 234, 'b': 678}, (7, 1, 3): {1, 3, 5, 7}, True: 1000}
print("_"*50)

################ set data type ############
"""
properties :

->  set is mutable data type
->  set can contains only immutable data type, int, float, string, tuple, boolean
->  set only store unique values
->  set does not follow any indexing, it store in random order.
"""

set1 = {4, 6, 7, 4.5, 'Hello', (4, 6, 7), 4, 4, 6, 6}

print(set1, type(set1)) # {4, 4.5, 6, 7, (4, 6, 7), 'Hello'} <class 'set'>

set2 = {4, 6, 8, 11, 22}
set2.add(400)
print(set2) # {400, 4, 6, 22, 8, 11}
print("_"*50)

#################### Boolean Data Type ############
"""
Properties:
->  Boolean is immutable data type
->  Boolean can consider with only values True or False
->  All the conditional output will be consider in boolean always
"""
var1 = True
print(var1, type(var1))  # True <class 'bool'>

var2 = False
print(var2, type(var2))  # False <class 'bool'>
print("_"*50)

school = {
    'teacher': {
        'math': [
                {'Name' : 'mohan', 'address' :  'Pune', 'email' : 'mohan@gmail.com'},
                {'Name' : 'rahul', 'address' :  'Mumbai', 'email' : 'rahul@gmail.com'},
                {'Name': 'mohit', 'address': 'Mumbai', 'email': 'mohit@gmail.com'}
        ],
        'english': [
                {'Name' : 'mohit', 'address' :  'Indore', 'email' : 'mohit@gmail.com'},
                {'Name' : 'raghu', 'address' :  'Chennai', 'email' : 'raghu@gmail.com'}
        ],
        'chemistry': [
                {'Name' : 'Aman', 'address' :  'Pune', 'email' : 'Aman@gmail.com'},
                {'Name' : 'subham', 'address' :  'Mumbai', 'email' : 'subham@gmail.com'}
        ],
        'physics' : [
                {'Name' : 'madhu', 'address' :  'Pune', 'email' : 'madhu@gmail.com'},
                {'Name' : 'shwetha', 'address' :  'Mumbai', 'email' : 'shwetha@gmail.com'}
        ]
    },
    'student': {}
}

# print(school['teacher']['english'][1]['email'])
print(school['teacher'])
print(school['teacher']['english'])

