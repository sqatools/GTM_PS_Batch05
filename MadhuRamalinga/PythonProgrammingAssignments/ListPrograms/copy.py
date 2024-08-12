# Program to copy the list to another list

list1 = [2, 4, 6]
new_list = list1.copy()

print(new_list) # [2, 4, 6]

########## OR ###########
print("_"*50)

list2 = [1, 6, 4]
copy_list = []

for val in list2:
    copy_list.append(val)

print(copy_list) # [1, 6, 4]
