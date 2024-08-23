# Create a list of tuples from a list having a number and its square in each tuple

list1 = [2, 5, 4]
tup1 = []

for val in list1:
    tup1.append((val,val**2))

print(tup1) # [(2, 4), (5, 25), (4, 16)]

############ OR ###############

list2 = [4,6,3,8]

tup = [(val, pow(val, 2)) for val in list2]
print(tup) # [(4, 16), (6, 36), (3, 9), (8, 64)]