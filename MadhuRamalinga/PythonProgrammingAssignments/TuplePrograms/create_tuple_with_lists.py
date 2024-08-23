# Program to create a tuple with 2 lists of data

list1 = [2, 4, 5]
list2 = [8, 1, 10, 14, 18]

tup = tuple(zip(list1,list2))

print(tup) # ((2, 8), (4, 1), (5, 10))