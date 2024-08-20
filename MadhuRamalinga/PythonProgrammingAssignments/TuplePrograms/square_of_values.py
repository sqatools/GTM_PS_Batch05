# Create a tuple having squares of the elements from the list

tup1 = (1, 8, 5, 4)
print("Original tuple:", tup1) # Original tuple: (1, 8, 5, 4)
tup1 = list(tup1)
a = list()

for val in tup1:
    b = val**2
    a.append(b)
tup1 = tuple(a)

print("Square of tuple values:", tup1) # Square of tuple values: (1, 64, 25, 16)