# Program to find the combination of 2 elements from the list
import itertools

list1 = [1, 2, 4, 5, 1, 8, 5, 8]
new_list = []
var = 10

for i in range(len(list1)): # len = 8, loop - 0, 1, 2, 3, 4, 5, 6, 7
    for val in itertools.combinations(list1,i):
        if sum(val) == var:
            new_list.append(val)

print(new_list) # [(2, 8), (2, 8), (5, 5), (1, 4, 5), (1, 4, 5), (1, 1, 8), (1, 1, 8), (4, 5, 1), (4, 1, 5)]
