# Python Program to create a dictionary from two lists

list1 = ['a', 'b', 'c', 'd']
list2 = [1, 3, 4, 5]
dict1 = {}

for val in range(len(list1)):
    dict1[list1[val]] = list2[val]

print(dict1) # {'a': 1, 'b': 3, 'c': 4, 'd': 5}

################ OR #################
print("_"*50)

for a, b in zip(list1,list2):
    dict1[a] = b

print(dict1) # {'a': 1, 'b': 3, 'c': 4, 'd': 5}
