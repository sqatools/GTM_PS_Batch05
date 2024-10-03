# 1.Dictionary program to add elements to the dictionary.
# dictionary = {}
# dictionary["Name"] = "Ketan"
# dictionary["Age"] = "21"
#
# print(dictionary)

# # 2.  Dictionary program to print the square of all values in a dictionary.
# dictionary = {'a': 5, 'b':3, 'c': 6, 'd': 8}
#
# for val in dictionary:
#     print(val,":", dictionary[val]**2)

# 3. Dictionary program to move items from dict1 to dict2
# D1 = {'name':'john','city':'Landon','country':'UK'}
# D2 = {}
#
# for val in D1:
#     D2[val] = D1[val]
#
# print(D2)

# # 4. Dictionary program to concatenate two dictionaries.
# dict1 = {'Name':'Harry','Rollno':345,'Address':'Jordan'}
# dict2 = {'Age':25,'salary': '$25k'}
#
# dict1.update(dict2)
#
# print(dict1)

# 5. Dictionary program to get a list of odd and even keys from the dictionary.
# dict1 = {1:25,5:'abc',8:'pqr',21:'xyz',12:'def',2:'utv'}
#
# list1 = [[val,dict1[val]] for val in dict1 if val%2 == 0]
# list2 = [[val,dict1[val]] for val in dict1 if val%2 != 0]
#
# print("Even key = ",list1)
# print("Odd key = ",list2)

# 6. Dictionary Program to create a dictionary from two lists.
# list1 = ['a','b','c','d','e']
# list2 = [12,23,24,25,15,16]
# dict1 = {}
#
# for a,b in zip(list1,list2):
#     dict1[a] = b
#
# print(dict1)

# 7.  Dictionary program to store squares of even and cubes of odd numbers in
# # a dictionary using dictionary comprehension.
# list1 = [4, 5, 6, 2, 1, 7, 11]
# dict1 = {}
#
# for val in list1:
#     if val % 2 == 0:
#         dict1[val] = val**2
#     else:
#         dict1[val] = val**3
#
# print(dict1)

# 8. Dictionary program to clear all items from the dictionary
# dict1 = {'Name':'Harry','Rollno':345,'Address':'Jordan'}
#
# dict1.clear()
# print(dict1)

# # 9. Dictionary program to remove duplicate values from Dictionary.
# dict1 = {'a':12,'b':2,'c':12,'d':5,'e':35,'f':5}
# dict2 = {}
#
# for key,val in dict1.items():
#     if val not in dict2.values():
#         dict2[key] = val
#
# print(dict2)

# 10.Dictionary program to create a dictionary from the string
# string = "SQAToolss"
# dict1 = {}
#
# for char in string:
#     dict1[char] = string.count(char)
#
# print(dict1)

# 11.Dictionary program to sort a dictionary in  python using values.
# dict1 = {'d':14,'b':52,'a':13,'c': 1}
#
# sorted_ = {key: value for key, value in
#              sorted(dict1.items(), key=lambda item: item[1])}
# print(sorted_)
# 12. Python Dictionary program to add a key in a dictionary.
# dict1 = {1:'a',2:'b'}
#
# dict1.update({3:'c'})
#
# print(dict1)
# 13.  Dictionary program to concatenate two dictionaries.
# dict1 = {'name':'yash','city':'pune'}
# dict2 =  {'course':'python','institute':'sqatools'}
#
# dict1.update(dict2)
#
# print(dict1)

# 14. Dictionary program to swap the values of the keys in the dictionary.
# D1 = {'name':'yash','city':'pune'}
# D2 ={}
#
# for key,value in D1.items():
#     D2[value] = key
#
# print(D2)

# 15. Dictionary program to get the sum of all the items in a dictionary.
# D1 =  {'x':23,'y':10,'z':7}
# total = 0
# for val in D1.values():
#     total += val
#
# print(total)
#
# 16.  program to get the size of a dictionary in python
# import sys
# D1 = {'name':'virat','sport':'cricket'}
#
# print("Size of dic1: " + str(sys.getsizeof(D1)) + "bytes")

# 17. Dictionary program to check whether a key exists in the dictionary or not.
# D1 = {'city':'pune','state':'maharashtra'}
# count = 0
#
# for key in D1.keys():
#     if key == "Country":
#         count += 1
#
# if count > 0:
#     print("Key exists")
# else:
#     print("Key does not exists")

# 18.  program to iterate over a dictionary.
# D1 = {'food':'burger','type':'fast food'}
#
# for val in D1:
#     print(val,D1[val])

# 19. Dictionary program to insert a key at the beginning of the dictionary
# dict1 = {'course':'python','institute':'sqatools' }
# dict2 = {'name':'omkar'}
#
# dict2.update(dict1)
#
# print(dict2)

# 20. Dictionary  program to create a dictionary where keys are between 1 to 5
# dict1 = {}
#
# for i in range(1,6):
#     dict1[i] = i**2
#
# print(dict1)