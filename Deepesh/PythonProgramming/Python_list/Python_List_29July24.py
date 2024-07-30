"""
# Properties:
-> list is mutable data type, once it is defined we can modify.
-> List is dynamic.
-> List can contains all type of data, int. float, string, list, tuple, dict, set, boolean
-> List follows positive and negative indexing
-> List values are comma separated values.
"""

############################## list Methods ##############################
print(dir(list))
"""
 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""

#### Add data to the list ####
print("_" * 50)
# append() method: This method add data at end of the list
list_f = [4, 6, 7, 2, 8]
list_f.append(100)
list_f.append(50)
list_f.append(25)
list_f.append([3, 5, 7])
list_f.append('Python')
print("list_f :", list_f)  # [4, 6, 7, 2, 8, 100, 50, 25, [3, 5, 7], 'Python']

print("_" * 50)
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

print("_" * 50)
## extend() method : This method combine the data from list1 to list2, and modify the existing list.
list1 = [4, 6, 7, 8]
list2 = ['a', 'b', 'c', 'd']

list2.extend(list1)
print("list2 :", list2)  # ['a', 'b', 'c', 'd', 4, 6, 7, 8]

str1 = "Hello"
print("-".join(str1))  # H-e-l-l-o

### list concatenation ####
# list concatenation combine two list and create new list instead of modify the existing list.
print("_" * 50)
list_a = [3, 6, 7, 2, 4]
list_b = ['a', 'b', 'c', 'd']

list_c = list_a + list_b
print("list_c :", list_c)
# [3, 6, 7, 2, 4, 'a', 'b', 'c', 'd']


### multiply list values ####
print("_" * 50)
list_e = [4, 7, 2]
list_f = list_e * 10
print("list values:", list_f)
# [4, 7, 2, 4, 7, 2, 4, 7, 2, 4, 7, 2, 4, 7, 2, 4, 7, 2, 4, 7, 2, 4, 7, 2, 4, 7, 2, 4, 7, 2]


############### Remove data from list #################

####
print("_" * 50)
# remove() method: This method will remove specific value the list and does not return it
list_h = [5, 7, 8, 2, 4, 5, 12]
list_h.remove(4)
list_h.remove(5)

print("list_h :", list_h)
# [7, 8, 2, 5, 12]


############
# pop() method : this method remove data from the list using specific index position and return the
#                 value, the default index position is -1

list_l = [4, 6, 1, 7, 2, 44, 22]
# remove from default index
val = list_l.pop()
print("removed value :", val)
print("list_l :", list_l)

val2 = list_l.pop(3)
print("removed value:", val2)

####################################
print("_" * 50)
# write a python program move data from one list to another list
list_t = [4, 6, 7, 81, 14]
list_y = []

for i in range(len(list_t)):
    val = list_t.pop(0)
    list_y.append(val)
print("list_t :", list_t)
print("list_y :", list_y)

#########
print("_" * 50)
# clear method : This method remove all the data from list

list_w = [3, 6, 8, 12, 34, 56]
list_w.clear()
print("list_w :", list_w)  # list_w : []

##### remove data from list using delete function ####
print("_" * 50)

list_q = [3, 6, 8, 22, 55, 12, 45]
del list_q[1:4]  # we can the slicing of the list to remove bunch of values

print("list_q :", list_q)  # [3, 55, 12, 45]

# remove entire list from memory
del list_q  # This will delete list_q from memory
# print("list_q :", list_q) # NameError: name 'list_q'


######### Data manupulation in the list #######
print("_" * 50)
# replace the list data
list_p = [4, 7, 2, 8, 12]

list_p[0] = 100
print("list_p :", list_p)  # : [100, 7, 2, 8, 12]

list_p[1:4] = ['a', 'b', 'c']
print("list_p :", list_p)  # [100, 'a', 'b', 'c', 12]



#### sorting of list data ######
print("_"*50)
# sort() method : This method sort the list data in ascending and descending order and
#                 update original list
list_r = [4, 6, 8, 1, 5, 12]

# list_r.sort() # sort the list data in ascending order
# print("list_r :", list_r) # [1, 4, 5, 6, 8, 12]

list_r.sort(reverse=True)  # sort the list data in descending order
print("list_r :", list_r)  # [12, 8, 6, 5, 4, 1]



##############
print("_"*50)
# sorted function() : This function take list values as input and sort the list
#                      data in ascending and descending order.

list_z = [3, 6, 1, 7, 2, 8, 12]
result1 = sorted(list_z) # ascending order
print("result1 :", result1) # [1, 2, 3, 6, 7, 8, 12]

result2 = sorted(list_z, reverse=True) # descending order
print("result2 :", result2)

print("list_z :", list_z) # [3, 6, 1, 7, 2, 8, 12]


########### reverse the list data ###############
print("_"*50)
### reverse() method : This method reverse the list data and modify the original list
list_v = [5, 7, 12, 80, 1, 3]
list_v.reverse()
print("list_v :", list_v) # [3, 1, 80, 12, 7, 5]


### reversed() function : This function will return reverse list values and does not modify
# the original list

list_m = [4, 7, 9, 1, 5, 23]
result = reversed(list_m)
print(list(result))  # [23, 5, 1, 9, 7, 4]
print("list_m :", list_m) # [4, 7, 9, 1, 5, 23]


#################### Get max, min, sum ########
print("_"*50)

list_a = [4, 6, 8, 2, 88, 22, 45]
print("max value :", max(list_a)) # 88
print("min value :", min(list_a)) # 2
print("sum of values :", sum(list_a)) # 175
