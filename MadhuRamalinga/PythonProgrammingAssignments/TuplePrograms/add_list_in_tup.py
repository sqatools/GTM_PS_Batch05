# Python tuple program to add a list in the tuple

list1 = [2, 5]
tup1 = [4, 8]

tup1 = list(tup1)
tup1 = tup1 + list1 # [4, 8, 2, 5]
tup1 = tuple(tup1)

print(tup1) # (4, 8, 2, 5)

######## OR #########

list2 = [12,67]
tup = (6,8,4)
result = tuple(list(tup) + list2)
print(result) # (6, 8, 4, 12, 67)