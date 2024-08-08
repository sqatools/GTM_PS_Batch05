############ Dictionary Methods ######################
# print(dir(dict))
#  'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop',
#  'popitem', 'setdefault', 'update', 'values']


#### add data to dictionary #####
dict1 = {}
dict1['Name'] = 'Mohit'

print("dict 1:", dict1)

print("_" * 50)
##########

# update() method : This method update data from dict1 to dict2
dict_a = {'a': 123, 'b': 456, 'c': 13}
dict_b = {'p': 555, 'q': 234, 'r': 888}

dict_b.update(dict_a)
print("dict_b :", dict_b)  # {'p': 555, 'q': 234, 'r': 888, 'a': 123, 'b': 456, 'c': 13}

####### Get data from dictionary #####
# get() method : This method return the value of specific key
dict_c = {'p': 555, 'q': 234, 'r': 888, 'a': 123, 'b': 456, 'c': 13}

print("b key value :", dict_c['b']) # b key value : 456
print("c key value :", dict_c.get("c")) # c key value : 13

print("_" * 50)
##########
# keys() and values() method : Keys method return the list of keys and values method return the
# list of values
dict_d = {'p': 555, 'q': 234, 'r': 888, 'a': 123, 'b': 456, 'c': 13}

print("List of keys :", dict_d.keys())  # ['p', 'q', 'r', 'a', 'b', 'c']
print("List of values :", dict_d.values())  # [555, 234, 888, 123, 456, 13]

print("_" * 50)
#######
# pop() method: This method remove specific data from dict with the help of key
# and return the value
dict_e = {'p': 555, 'q': 234, 'r': 888, 'a': 123, 'b': 456, 'c': 13}

value = dict_e.pop('a')
print("value of a :", value)  # value of a : 123
print(dict_e)  # {'p': 555, 'q': 234, 'r': 888, 'b': 456, 'c': 13}

print("_" * 50)
#######
# popitem method: This method remove the key and value in one go and return it as tuple
dict_f = {'p': 555, 'q': 234, 'r': 888, 'a': 123, 'b': 456, 'c': 13}
dict_data = dict_f.popitem()
print("removed data from dict :", dict_data)  # ('c', 13)
print("update dict :", dict_f)  # {'p': 555, 'q': 234, 'r': 888, 'a': 123, 'b': 456}


print("_" * 50)
##############
# clear() method : This method remove all the data from dictionary
dict_g = {'p': 555, 'q': 234, 'r': 888, 'a': 123, 'b': 456, 'c': 13}
dict_g['p'] = None  # replace the exiting value with None
dict_g.clear()  # clear all the data from dictionary
print("dict_g :", dict_g) # dict_g : {}


print("_"*50)
##############
# delete function
dict_h = {'p': 555, 'q': 234, 'r': 888, 'a': 123, 'b': 456, 'c': 13}
del dict_h
#print("dict_h :", dict_h) # NameError: name 'dict_h'

dict_k = {'p' : 222, 'q' : 777, 'r' : 154}
del dict_k['p']
print("dict_k :", dict_k)  # {'q': 777, 'r': 154}

print("_"*60)
#######
# fromkeys method This method creates the dictionary with list keys and value as parameter in the method.
data = dict.fromkeys(['s','t', 'u', 'v'], 700)
print("result_dict :", data)  # {'s': 700, 't': 700, 'u': 700, 'v': 700}

print("_"*50)
#####
# setdefault : This method assign new key value to dict if key is not available, else return the key value.

dict_q = {'a' : 111, 'b': 222, 'c' : 333}
result = dict_q.setdefault("d", 444)
result2 = dict_q.setdefault("b", 500)

print("result :", result, result2) # 444 222
print("dict_q :", dict_q) # {'a': 111, 'b': 222, 'c': 333, 'd': 444}



print("_"*50)
############### Deep copy and shallow copy concept in the dictionary #######

# Shallow copy
dict_r = {'Name' : 'Rahul', 'email' : 'rahul@gmail.com', 'phone' : 34566554}
dict_y = dict_r
dict_y['city'] = 'Mumbai'
print("dict_y :", dict_y) # {'Name': 'Rahul', 'email': 'rahul@gmail.com', 'phone': 34566554, 'city': 'Mumbai'}
print("dict_r :", dict_r) # {'Name': 'Rahul', 'email': 'rahul@gmail.com', 'phone': 34566554, 'city': 'Mumbai'}


print("_"*50)
#### Deep copy ####

dict_x = {'a' : 123, 'b' : 567, 'c' : 134}
dict_z = dict_x.copy()
dict_z['d'] = 600

print("dict x :", dict_x) # {'a': 123, 'b': 567, 'c': 134}
print("dict z :", dict_z) # {'a': 123, 'b': 567, 'c': 134, 'd': 600}


print("_"*50)
#######
# write a python program to check list of values in divisible by 3 or 5
# if divisible by 3 then add 'fizz' as value
# if divisible by 5 then add 'buzz' as value
# if divisible by both then add 'fizzbuzz'

list_a = [3, 6, 12, 25, 30]
#output = {3 : 'fizz', 6 : 'fizz', 12: 'fizz', 25: 'buzz', 30: 'fizzbuzz'}

result_data = {}

for val in list_a:
    if val%3 == 0 and val%5 == 0:
        result_data[val] = 'fizzbuzz'
    elif val%3 == 0:
        result_data[val] = 'fizz'
    elif val%5 == 0:
        result_data[val] = 'buzz'

print("result data :", result_data)
# {3: 'fizz', 6: 'fizz', 12: 'fizz', 25: 'buzz', 30: 'fizzbuzz'} '''