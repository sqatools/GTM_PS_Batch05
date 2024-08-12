# Store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.

list1 = [1, 3, 2, 4, 5, 8]
dict1 = {}

for val in list1:
    if val%2 == 0:
        dict1[val] = val**2
    else:
        dict1[val] = val**3

print(dict1) # {1: 1, 3: 27, 2: 4, 4: 16, 5: 125, 8: 64}
