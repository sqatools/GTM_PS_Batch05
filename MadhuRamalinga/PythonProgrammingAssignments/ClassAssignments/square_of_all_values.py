#loop comprehension#

list1 = [2, 1, 4, 5, 8]
result = [val**2 for val in list1]
print("Square of given numbers are :", result)

nested_result = [(a, b) for a in range(3) for b in ['x', 'y', 'z']]
print("nested for loop is:", nested_result)

list_2 = [2, 1, 4, 5, 8, 10]
result1 = [val for val in list_2 if val % 2 == 0]
print("Even numbers are:", result1)