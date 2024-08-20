# Convert a list into a tuple and multiply each element by 2

list1 = [4, 2, 8]
list2 = []

for val in list1:
    a = val * 2
    list2.append(a)

tup1 = tuple(list2)
print("Original list:", list1)
print("After multiplying by 2:",tup1)

# Original list: [4, 2, 8]
# After multiplying by 2: (8, 4, 16)

