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

print("_"*50)
# Add method : This method add one value at a time in the set
set_a = {3, 6, 71, 2}
set_a.add(100)

print("set_a :", set_a)  #  {2, 3, 100, 6, 71}


print("_"*50)
#######
# update method : This method update one set data to another and update origin set
set_b = {3, 6, 8, 1}
set_c = {'a', 'b', 'c', 'd'}

set_c.update(set_b)
print("set_c :", set_c)  # {1, 3, 6, 8, 'd', 'b', 'a', 'c'}



#########
# union method: This method combine 2 sets and create another set.
set_f = {3, 6, 8, 1}
set_g = {'p', 'q', 'r', 's'}

result = set_f.union(set_g)
print("result :", result)  # {1, 3, 6, 8, 'p', 'q', 'r', 's'}
print("set_f :", set_f) # {8, 1, 3, 6}
print("set_g :", set_g) # {'r', 'q', 's', 'p'}
