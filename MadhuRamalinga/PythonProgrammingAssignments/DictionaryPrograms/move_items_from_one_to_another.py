# Move items from one dictionary to another

dict1 = {'Name' : 'Coco', 'Place' : 'Texas', 'Country' : 'USA'}
dict2 = dict1.copy()

print(dict2) # {'Name': 'Coco', 'Place': 'Texas', 'Country': 'USA'}
print(dict1) # {'Name': 'Coco', 'Place': 'Texas', 'Country': 'USA'}

############# OR ##############

dict3 = {'Name' : 'Coco', 'Place' : 'Texas', 'Country' : 'USA'}
dict4 = {}

for val in dict3:
    dict4[val] = dict3[val]

print(dict4) # {'Name': 'Coco', 'Place': 'Texas', 'Country': 'USA'}