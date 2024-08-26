# Program to print list after removing certain elements

list1 = [1, 3, 4, 5, 8]
new_list = []

for val in list1:
    if val != 3:
        new_list.append(val)
print("New list after removing certain elements are:",new_list) # New list after removing certain elements are: [1, 4, 5, 8]

################## Using List Comprehension ###################
print("_"*50)

list2 = [1, 3, 4, 5, 8]
new_list1 = []

new_list1 = [val1 for val1 in list2 if val1 != 3]

print("New list after removing certain elements are:",new_list1) # New list after removing certain elements are: [1, 4, 5, 8]