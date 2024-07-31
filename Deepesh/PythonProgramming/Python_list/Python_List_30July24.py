"""
# Properties:
-> list is mutable data type, once it is defined we can modify.
-> List is dynamic.
-> List can contains all type of data, int. float, string, list, tuple, dict, set, boolean
-> List follows positive and negative indexing
-> List values are comma separated values.
"""
# Deep copy and shallow copy

# shallow copy
list_a = [3, 6, 2, 7, 1, 5]
list_b = list_a
list_b.append(100)
list_c = list_b
list_c.append(400)

print("List_b :", list_b) # [3, 6, 2, 7, 1, 5, 100, 400]
print("List_a :", list_a) # [3, 6, 2, 7, 1, 5, 100, 400]
print("List_c :", list_c) # [3, 6, 2, 7, 1, 5, 100, 400]

### Deep Copy ####

list_p = [4, 7, 2, 8, 1, 9, 23]
list_q = list_p.copy()
list_q.append(100)

print("list_p :", list_p) # [4, 7, 2, 8, 1, 9, 23]
print("list_q :", list_q) # [4, 7, 2, 8, 1, 9, 23, 100]

######### list comprehension ########
print("_"*50)
# get square of all the values
list_r = [4, 6, 2, 3, 7, 1, 8, 23]
result = []
for val in list_r:
    result.append(val**2)

print("result:", result)

# solution with list comprehension

result2 = [val**2 for val in list_r]
print("result2 :", result2)

#####
print("_"*50)
# nested loop with list comprehension

result_nested = [(x, y) for x in range(3) for y in ['a', 'b', 'c']]
print("nested for loop:", result_nested)
# [(0, 'a'), (0, 'b'), (0, 'c'), (1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c')]

######
print("_"*50)
# write python program to get all even values from given list

list_n = [4, 6, 7, 1, 3, 8, 24]
even_value = []

for val in list_n:
    if val%2 == 0:
        even_value.append(val)
print("even values :", even_value)

# solution with list comprehension
even_value_result = [val for val in list_n if val%2 == 0]
print("even values result :", even_value_result)


# write a python get below output:
print("_"*50)
list_n = [4, 6, 7, 1, 3, 8, 24]
# result = [(4, 'even'), (6, 'even'), (7, 'odd'), (1, "odd"), (3, 'odd') (8,'even'), (24, 'even')]

result4 = [(val, 'even') if val%2 == 0 else (val, 'odd') for val in list_n]
print("result4 :", result4)


# Q1 : Write a python program to change reverse each values in given list
list2 = ['Hello', 'Python', 'Programs']
# output = ['olleH', 'nohtyP', 'smargorP']

# Q2 Write a python program to find out the second-highest number from list
list1 = [3, 6, 12, 45, 223, 56]
# output = 56

print("_"*50)
# Q1 : Write a python program to change reverse each values in given list
list_a = ['Hello', 'Python', 'Programs']
# output = ['olleH', 'nohtyP', 'smargorP']

output = []
for word in list_a:
    #print(word[::-1])
    output.append(word[::-1])

print("output :", output)


# # Q2 Write a python program to find out the second-highest number from list
list_b = [3, 6, 12, 45, 223, 56]
# # output = 56
max_val = 0 # 3, 6, 12, 45, 223, 56
sec_max_val = 0

for val in list_b: # 3, 6
    if val > max_val:
        max_val = val # 3, 6, 56
    elif val < max_val and val > sec_max_val:
        sec_max_val = val

print("max value :", max_val)
print("sec max value :", sec_max_val)

