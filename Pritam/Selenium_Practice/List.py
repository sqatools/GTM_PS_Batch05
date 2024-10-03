# 1.  program to calculate the square of each number from the given list.
# list1 = [3, 5, 7, 1, 8]
#
# for val in list1:
#     print(val, ":", val**2)

# 2. program to combine two lists.
# list1 = [3, 6, 7, 81, 2]
# list2 = [11, 15, 17, 13]
#
# output = list1 + list2
#
# print(output)

# 3. program to calculate the sum of all elements from a list.
# list1 = [2,5,8,0,1]
# var = 0
#
# for value in list1:
#     var += value
#
# print(var)

# 4. program to find a product of all elements from a given list.
# list1 = [3,6,9,2]
#
# var = 1
#
# for value in list1:
#     var *= value
#
# print(var)

# # 5. program to find the minimum and maximum elements from the list.
# list1 = [23,56,12,89]
# list1.sort()
# print("Smallest number: ", list1[0])
# print("Largest number: ", list1[-1])

# 6. program to differentiate even and odd elements from the given list.
# og_list = [23,11,78,90,34,55]
# odd = []
# even = []
#
# for value in og_list:
#     if value%2 == 0:
#         even.append(value)
#     else:
#         odd.append(value)
# print("Even numbers: ", even)
# print("Odd numbers: ", odd)

# 7.  program to remove all duplicate elements from the list.
# list1 = [5,7,8,2,5,0,7,2]
#
# list2 = []
#
# for value in list1:
#     if value not in list2:
#         list2.append(value)
# print(list2)

# 8. program to print a combination of 2 elements from the list whose sum is 10
import itertools

# list1 = [2,5,8,5,1,9]
#
# var = 10
#
# list3 = []
#
# for i in range(len(list1)):
#     for combi in itertools.combinations(list1,i):
#         if sum(combi) == var:
#             list3.append(combi)
# print(list3)

# 9.  program to print squares of all even numbers in a list..
# list1 = [2,4,7,8,5,1,6]
#
# for value in list1:
#     if value%2 == 0:
#
#         print(value,":",value**2)

# 10. program to split the list into two-part, the left side all odd values
# and the right side all even values.
# list1 = [5, 7, 2, 8, 11, 12, 17, 19, 22]
#
# even = []
# odd = []
#
# for value in list1:
#     if value%2 == 0:
#         even.append(value)
#     else:
#         odd.append(value)
#
# odd.extend(even)
#
# print(odd)
# 11.  program to get common elements from two lists
# list1 = [4, 5, 7, 9, 2, 1]
# list2 = [2, 5, 8, 3, 4, 7]
#
# common_list = []
# for value in list1:
#     if value in list2:
#         common_list.append(value)
#
# print(common_list)

# 12.  program to reverse a list with for loop
# list1 = [1,2,3,4,55]
# for i in range(len(list1)-1,-1,-1):
#     print(list1[i], end=" ")

# 13.  program to reverse a list with a while loop.
# list1 = [1,2,3,4,5,6]
# count = len(a)-1
#
# while count >= 0:
#     print(value[count], end=" ")
#     count -= 1

# 14.program to reverse a list using index slicing
# list1 = [2,4,6,8]
# list2 = list1[::-1]
# print(list2)

# 15.program to reverse a list with reversed and reverse methods.
#
# list1 = [2,3,7,9,3,1]
# print("Using reversed: ",list(reversed(list1)))

# 16.  program to copy or clone one list to another list
# list1 = [1,2,4,7,0,5]
# list2 = []
#
# for value in list1:
#     list2.append(value)
#
# print(list2)