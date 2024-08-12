# Program to get a list of odd and even keys from the dictionary

dict1 ={1 : 'abc', 3 : 'def', 2 : 'pqr', 4 : 'xyz'}
even = []
odd = []

for val in dict1:
    if val%2 == 0:
        even.append([val, dict1[val]])
    else:
        odd.append([val, dict1[val]])

print("Even key: ", even)
print("Odd key:", odd)

# Even key:  [[2, 'pqr'], [4, 'xyz']]
# Odd key: [[1, 'abc'], [3, 'def']]

############## OR ################
print("_"*50)

dict2 = {1:25,5:'abc',8:'pqr',21:'xyz',12:'def',2:'utv'}

list1 = [[val,dict2[val]] for val in dict2 if val%2 == 0]
list2 = [[val,dict2[val]] for val in dict2 if val%2 != 0]

print("Even key = ",list1)
print("Odd key = ",list2)

# Even key =  [[8, 'pqr'], [12, 'def'], [2, 'utv']]
# Odd key =  [[1, 25], [5, 'abc'], [21, 'xyz']]
