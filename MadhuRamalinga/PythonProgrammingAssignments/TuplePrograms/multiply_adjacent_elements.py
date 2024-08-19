# Python tuple program to multiply adjacent elements of a tuple

tup1 = (1, 8, 5, 4)
list1 = []

for a, b in zip(tup1,tup1[1:]):
    c = a*b
    list1.append(c)
tup1 = tuple(list1)

print("Multiplication of adjacent values are:", tup1) # Multiplication of adjacent values are: (8, 40, 20)