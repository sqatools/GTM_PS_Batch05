# Program to swap the values of the keys in the dictionary

dict1 = {'Name' : 'Coco', 'Age' : '1'}
dict2 = {}

for key,val in dict1.items():
    dict2[val] = key

print(dict2) # {'Coco': 'name', '1': 'Age'}
