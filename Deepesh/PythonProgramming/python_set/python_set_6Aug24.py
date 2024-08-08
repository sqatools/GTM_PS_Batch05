"""
# properties of the set
-> its mutable data type
-> it store only unique value
-> does not follow any indexing
-> it store the data in random order
-> set can only immutable data type as member e.g int, float, string, tuple, boolean
"""

set1 = {3, 5, 7.5, 2, 3, 2, 'hello', (3, 5, 7), True}
print(set1, type(set1)) # {(3, 5, 7), 2, 3, 'hello', 5, True, 7.5} <class 'set'>

print("_"*50)
# apply loop on the set
for val in set1:
    print(val)

"""
(3, 5, 7)
2
3
True
5
7.5
hello
"""
##################################
# Set methods:
print(dir(set))
"""
'add', 'clear', 'copy', 'difference', 
'difference_update', 'discard', 'intersection',
 'intersection_update', 'isdisjoint', 'issubset', 
 'issuperset', 'pop', 'remove', 'symmetric_difference', 
 'symmetric_difference_update', 'union', 'update']
"""

#######
# remove method : This method remove specific value from set
set_a = {3, 6, 1, 7, 23, 8}
set_a.remove(23)
print("set_a:", set_a)

# remove the value which is not available in the set
#set_a.remove(25) # KeyError: 25


print("_"*50)
#######
# discard method : This method also remove specific value from set, and does not through any error
#                  if the data is not available in the set

set_b = {4, 6, 1, 7, 2, 5, 16}
set_b.discard(7)
print("set_b :", set_b)

# if specific value is not available in the set, then discard method doesn't through error.
set_b.discard(25)


print("_"*50)
#############
# pop() method: This method pop the value from set and return it
set_c = {'a', 'b', 'c', 4, 6, 2, 7, 12, 45}
output = set_c.pop()
print("removed value :", output) # b
print("set_c :", set_c) # {2, 4, 6, 7, 12, 45, 'c', 'a'}


print("_"*50)
##################
# intersection() method : This method helps to find the common values between 2 sets
set_p = {3, 5, 7, 9, 12, 'a'}
set_q = {'a', 'b', 3, 12, 'c', 'd'}

result = set_p.intersection(set_q)
print("intersection values in 2 sets :", result)  #  {'a', 3, 12}
print("set_p :", set_p) #  {'a', 3, 5, 7, 9, 12}
print("set_q :", set_q) # {'d', 'a', 'c', 3, 12, 'b'}

print("_"*50)
# intersection_update : This method update the any specific set with intersection result

set_p.intersection_update(set_q)
print("set_p :", set_p)  # {3, 12, 'a'}
print("set_q :", set_q) # {'d', 'a', 'c', 3, 12, 'b'}


print("_"*50)
#################
# difference method: This method find out the difference values from specific set
set_x = {3, 5, 7, 9, 12, 'a'}
set_y = {'a', 'b', 3, 12, 'c', 'd'}

diff_Result = set_x.difference(set_y)
print("difference result :", diff_Result) # {9, 5, 7}

print("set_X :", set_x) # {3, 5, 'a', 7, 9, 12}
print("set_y :", set_y) # {3, 'd', 'c', 'a', 'b', 12}

print("_"*50)
# difference_update(): This method update difference result to specific set
set_x.difference_update(set_y)

print("set_X :", set_x) # {5, 7, 9}
print("set_y :", set_y) # {3, 'd', 'c', 'a', 'b', 12}



print("_"*50)
#################
# symmetric_difference: This method provide the difference of the both sets.

set_q = {3, 5, 7, 9, 12, 'a'}
set_r = {'a', 'b', 3, 12, 'c', 'd'}

sym_diff_result = set_q.symmetric_difference(set_r)
print("sym diff update result :", sym_diff_result)

# symmetric_difference_update : This method update the symmetric_difference result to specific set.
set_q.symmetric_difference_update(set_r)
print("set_q :", set_q) # {5, 7, 9, 'd', 'c', 'b'}
print("set_r :", set_r) # {3, 'b', 'a', 12, 'd', 'c'}


print("_"*50)
########
# issubset and issuperset method : This method find the superset and subset from given sets values

set_m = {3, 6, 8, 2, 5, 1}
set_n = {3, 6, 5}
set_o = {6, 1, 25}

print("check for superset for set_m with set_n:", set_m.issuperset(set_n)) # True
print("check for superset for set_m with set_o :", set_m.issuperset(set_o)) # False
print("check for subset set_n with set_m:", set_n.issubset(set_m)) # True
print("check for subset set_o with set_m:", set_o.issubset(set_m)) # False

print("_"*40)
####################
# isdisjoint() method : This method return True if there is no common values between 2 sets.

set_A = {3, 5, 7, 9, 12, 'a'}
set_B = {'a', 'b', 3, 12, 'c', 'd'}
set_C = {'p', 'q', 'r', 's'}

result = set_A.isdisjoint(set_B)
print("is disjoint result set_A with set_B:", result)  # False
print("is disjoint result set_A with set_C:", set_A.isdisjoint(set_C))  # True
print("is disjoint result set_B with set_C:", set_B.isdisjoint(set_C))  # True


#######
# clear method : This method remove all the data from sets
set_D = {3, 5, 7, 9, 12, 'a'}
set_E = {'a', 'b', 3, 12, 'c', 'd'}
set_D.clear()
print("set_D :", set_D) # set()

del set_E  # remove the set variable from memory
# print("set_E :", set_E) # NameError: name 'set_E'


print("_"*50)
###############
# shallow copy
set_1 = {4, 7, 9, 1}
set_2 = set_1
set_2.add(100)

print("set_1 :", set_1) # {1, 100, 4, 7, 9}
print("set_2 :", set_2) # {1, 100, 4, 7, 9}


print("_"*40)
##### Deep copy #####
set_j = {4, 7, 9, 12}
set_k = set_j.copy()
set_k.add(200)
print("set_k :", set_k) # {4, 7, 200, 9, 12}
print("set_j :", set_j) # {9, 4, 12, 7}
