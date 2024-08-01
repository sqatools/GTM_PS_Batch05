"""
Properties of dict :
-> Dict is mutable data type
-> Dict does not have indexing
-> Dict store in key value pair
-> Duplicate keys are not allowed
-> Dict can contain duplicate values
-> Dict allow all data type as value
-> Only Immutable data type can be key in the dictionary. e.g. int, float, string, tuple, boolean
-> Dict follows the LIFO (LAST IN FIRST OUT)
"""

dict1 = {'a' : 123, 'b' : 456, 'c' : 234}
print(dict1)

print(dict1['a']) # 123

# add data to dictionary
dict1['d'] = 400
print("dict1 :", dict1)

dict2 = {'p' : 123, 'q' : 456, 'r' : 900}

for data in dict2.items():
    print(data)

"""
('p', 123)
('q', 456)
('r', 900)
"""

for key, val in dict2.items():
    print("Key :", key, "value :", val)

"""
Key : p value : 123
Key : q value : 456
Key : r value : 900
"""

print("_"*50)
# Add different type of data to dict
dict3 = {}
dict3[23] = 456  # int
dict3[4.5] = 80.23 # float
dict3['a'] = 'Hello' # string
print("dict3 :", dict3)
#dict3[[2, 4, 5]] = [2, 7, 3, 6]  # unhashable type: 'list'

dict3[(3, 5, 2)] = [3, 6, 1, 7, 12]
print("dict3 :", dict3) # {23: 456, 4.5: 80.23, 'a': 'Hello', (3, 5, 2): [3, 6, 1, 7, 12]}

# dict3[{'a': 123}] = 'programming'  # unhashable type: 'dict'
dict3['Python'] = {'name' : 'john', 'email' : 'john@gmail.com', 'phone' : 3543543}
print(dict3)
# {23: 456, 4.5: 80.23, 'a': 'Hello', (3, 5, 2): [3, 6, 1, 7, 12], 'Python': {'name': 'john', 'email': 'john@gmail.com', 'phone': 3543543}}

dict3[True] = False
#dict3[{4, 7, 23}] = 543534 # unhashable type: 'set'
dict3[45] = {3, 5, 6, 1}

print("dict3 :", dict3)

# {23: 456, 4.5: 80.23, 'a': 'Hello', (3, 5, 2): [3, 6, 1, 7, 12], 'Python': {'name': 'john', 'email': 'john@gmail.com', 'phone': 3543543}, True: False, 45: {1, 3, 5, 6}}

print("_"*50)
############Dictionary Methods ######################
print(dir(dict))
#  'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop',
#  'popitem', 'setdefault', 'update', 'values']


