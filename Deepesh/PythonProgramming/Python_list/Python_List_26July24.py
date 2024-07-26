"""
# Properties:
-> list is mutable data type, once it is defined we can modify.
-> List is dynamic.
-> List can contains all type of data, int. float, string, list, tuple, dict, set, boolean
-> List follows positive and negative indexing
-> List values are comma separated values.
"""

list_a = [4, 5, 7, 11.45, 'Hello',[4, 6, 7, [4, 6, [12, 56]]], (2, 6, 8), {'a': 123, 'b' : 456}, True, {4, 7, 8}]
print(list_a)

# get value with indexing
print(list_a[4])  # Hello

print(list_a[-4][-1]) # 8
print(list_a[5][3][2][1]) # 56

print("_"*40)
## apply loop on the list value
list_b = [5, 7, 9, 2, 15]
for val in list_b:
    print(val)

print("_"*40)
# apply loop with index position
list_c = [3, 7, 1, 8, 11, 33]
for i in range(len(list_c)):
    print(i, list_c[i])

print("_"*50)
################# Slicing in list ######################

list_d = [3, 6, 8, 'a', 'b', 'c', 'Hello', 'Python']

print(list_d[4:7])  # ['b', 'c', 'Hello']

print(list_d[-2:-7:-1])  # ['Hello', 'c', 'b', 'a', 8]

print(list_d[1::2]) # [6, 'a', 'c', 'Python']

print(list_d[::-2]) # ['Python', 'c', 'a', 6]

print(list_d[-1:-len(list_d)-1: -2])  # ['Python', 'c', 'a', 6]

print(list_d[::-1]) # ['Python', 'Hello', 'c', 'b', 'a', 8, 6, 3]

print("_"*50)
############################## list Methods ##############################
print(dir(list))
"""
 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""

#### Add data to the list ####
print("_"*50)
# append() method: This method add data at end of the list
list_f = [4, 6, 7, 2, 8]
list_f.append(100)
list_f.append(50)
list_f.append(25)
list_f.append([3, 5, 7])
list_f.append('Python')
print("list_f :", list_f)  # [4, 6, 7, 2, 8, 100, 50, 25, [3, 5, 7], 'Python']


print("_"*50)
# insert() method : This method add data to the list at specific index position.
list_h = [3, 6, 8, 1, 2, 4]
list_h.insert(2, "P")
list_h.insert(-1, 500)
list_h.insert(0, 100)
print("list_h :", list_h)
# [100, 3, 6, 'P', 8, 1, 2, 500, 4]

list_j = [4, 6, 8, 2]
list_j.insert(-2, 25)
print("list_j :", list_j)


print("_"*50)
## extend() method : This method combine the data from list1 to list2, and modify the existing list.
list1 = [4, 6, 7, 8]
list2 = ['a', 'b', 'c', 'd']

list2.extend(list1)
print("list2 :", list2) # ['a', 'b', 'c', 'd', 4, 6, 7, 8]

str1= "Hello"
print("-".join(str1)) # H-e-l-l-o
