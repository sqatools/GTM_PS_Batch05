# Python tuple program to add an item to a tuple

tup1 = (1, 8, 5)
print("Exisitng tuple:", tup1)
tup1 = list(tup1)
tup1.append(10)
tup1 = tuple(tup1)
print("New Tuple:", tup1)

# Exisitng tuple: (1, 8, 5)
# New Tuple: (1, 8, 5, 10)