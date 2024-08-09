# Program to split the list into two-part

list1 = [1, 10, 5, 4, 8, 2, 5]
even = []
odd = []

for val in list1:
    if val % 2 == 0:
        even.append(val)
    else:
        odd.append(val)

# print(even) # [10, 4, 8, 2]
# print(odd) # [1, 5, 5]

odd.extend(even)
print(odd) # [1, 5, 5, 10, 4, 8, 2]