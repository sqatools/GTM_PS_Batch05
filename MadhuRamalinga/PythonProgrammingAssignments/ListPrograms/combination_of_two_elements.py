# Program to find the combination of 2 elements from the list whose sum is 10
import itertools

list1 = [0, 1, 0, 2, 4, 6, 3, 9, 5, 8]
new_list = []
var = 10

# for i in range(len(list1)): # len = 8, i = 0, 1, 2, 3, 4, 5, 6, 7
#     for val in itertools.combinations(list1,i):
#         if sum(val) == var:
#             new_list.append(val)
#
# print(new_list) # [(2, 8), (2, 8), (5, 5), (1, 4, 5), (1, 4, 5), (1, 1, 8), (1, 1, 8), (4, 5, 1), (4, 1, 5)]

for i in range(len(list1)):
    for j in range(i+1, len(list1)):
        if list1[i] + list1[j] == 10:
            print(list1[i], list1[j])
            new_list.append([list1[i], list1[j]])
        else:
            continue

for i in range(len(list1)):
    for j in range(i+1, len(list1)):
        for k in range(j+1, len(list1)):
            if list1[i] + list1[j] + list1[k] == 10:
                print(list1[i], list1[j], list1[k])
                new_list.append([list1[i] , list1[j], list1[k]])

            else:
                continue

print("new list :", new_list )


