# Python tuple program to remove an item from a tuple

tup1 = (1, 8, 5, 4)
list1 = list(tup1)
list1.remove(1)
# print(list1) # [8, 5, 4]

tup1 = tuple(list1)

print("Tuple values after removing 1:",tup1) # Tuple values after removing 1: (8, 5, 4)