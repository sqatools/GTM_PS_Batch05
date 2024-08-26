# Get the sum of all the items in a dictionary

dict1 = {'a' : 10, 'b' : 30, 'c' : 60}
total = 0

for val in dict1.values():
    total += val

print(total) # 100