# Program to get common elements from two lists.

list1 = [1, 2, 4, 5, 8, 10]
list2 = [3, 4, 5, 10, 18, 1]
new_list = []

for val in list1:
    if val in list2:
        new_list.append(val)
print(new_list) # [1, 4, 5, 10]