# Program to remove negative elements from the list

list1 = [-1, 10, 8, 14, -4, -5, 0]
new_list= []

for val in list1:
    if val >= 0:
        new_list.append(val)
print(new_list) # [10, 8, 14]