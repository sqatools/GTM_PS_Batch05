# Program to remove all the duplicate elements from a list

list1 = [4, 5, 8, 10, 18, 10, 25, 5, 8]
new_list = []

for val in list1:
    if val not in new_list:
        new_list.append(val)

print("List values after removing the duplicates are: ", new_list) # List values after removing the duplicates are:  [4, 5, 8, 10, 18, 25]