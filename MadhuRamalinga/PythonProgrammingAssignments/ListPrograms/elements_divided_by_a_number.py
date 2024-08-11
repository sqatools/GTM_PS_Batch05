# Program to get a list of elements divided by a number

list1 = [4, 21, 2, 25, 16, 38, 14]
new_list = []

for val in list1:
    if val%2 == 0:
        new_list.append(val)

print(new_list)

################# OR #################
print("_"*50)

list2 = [3,7,0,2,6,14,88,21]

#Creating empty list
list3 = []

for value in list2:
    if value%3 == 0 or value%7 == 0:
        list3.append(value)

print(list3)