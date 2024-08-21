# Check whether a key exists in the dictionary or not.

dict1 = {'Name' : 'Coco', 'Age' : '1'}
count = 0

for key in dict1.keys():
    if key == 'City':
        count += 1
if count > 0:
    print("Key exists")
else:
    print("Key does not exists") # Key does not exists
