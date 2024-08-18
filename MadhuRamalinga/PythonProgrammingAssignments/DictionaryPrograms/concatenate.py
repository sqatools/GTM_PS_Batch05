# Python program to concatenate two dictionaries to from a single dictionary

dict1 = {'name' : 'Coco', 'Age' : '1'}
dict2 = {'DOB' : 'Nov 2023'}

dict1.update(dict2)

print(dict1) # {'name': 'Coco', 'Age': '1', 'DOB': 'Nov 2023'}