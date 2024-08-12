# Python program to remove duplicate values from Dictionary.

dict1 = {'a' : 1, 'b' : 2, 'c' : 1, 'd' : 2, 'e' : 5}
new_dict = {}

for key,val in dict1.items():
    if val not in new_dict.values():
        new_dict[key] = val

print(new_dict) # {'a': 1, 'b': 2, 'e': 5}