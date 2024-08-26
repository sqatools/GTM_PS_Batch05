# Python program to create a dictionary in the given form of (n^3)

dict1 = {}

for val in range(1, 5):
    dict1.update({val:val**3})

print(dict1) # {1: 1, 2: 8, 3: 27, 4: 64}

############## OR #################

n = 4
D1 = {}

for i in range(1,4+1):
    D1.update({i:i**3})

print(D1)