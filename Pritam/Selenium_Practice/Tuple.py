# # 1.  Python tuple program to create a tuple with 2 lists of data.
# list1 = [4, 6, 8]
# list2 = [7, 1, 4]
# tup =tuple(zip(list1,list2))
# print(tup)
# 2. Python tuple program to find the maximum value from a tuple
# tup = (41, 15, 69, 55)
# print("Maximum value: ",max(tup))
# 3. Python tuple program to find the minimum value from a tuple
# tup = (36,5,79,25)
# print("Minimum value: ",min(tup))
# 4. Python tuple program to create a list of tuples from a list having
# a number and its square in each tuple.
# list1 = [4,6,3,8]
#
# tup = [(val, pow(val, 2)) for val in list1]
# print(tup)
# 5. Python tuple program to create a tuple with different datatypes.
# tup = (2.6,1,'Python',True,[5, 6, 7],(5, 1, 4),{'a':123,'b':456})
# print("Tuple: ",tup)
# 6. Python tuple program to create a tuple and find an element from it by its index no.
# tup = (4,8,9,1)
# print("Number in the tuple with index 2: ",tup[2])
# 7. Python tuple program to assign values of tuples to several variables and print them.
# tup =  (6,7,3)
# (a,b,c) = tup
# print("a: ",a)
# print("b: ",b)
# print("c: ",c)
# 8. Python tuple program to add an item to a tuple
# tup = (18,65,3,45)
# print("Old tuple: ",tup)
# tup = list(tup)
# tup.append(15)
# tup = tuple(tup)
# print("New tuple: ",tup)
# 9. Python tuple program to convert a tuple into a string
# tup = ('s','q','a','t','o','o','l','s')
# str1 = ''
# for char in tup:
#     str1 += char
#
# print("String: ",str1)
# 10. Python tuple program to get the 2nd element from the front and
# the 3rd element from the back of the tuple.
# tup = ('s','q','a','t','o','o','l','s')
# print("2nd element from the front in the String: ",tup[1])
# print("3rd element from the last in the String: ",tup[-3])

# 11. Python tuple program to check whether an element exists in a tuple or not.
# tup = ('p','y','t','h','o','n')
# if 'p' in tup:
#     print("True")
# else:
#     print("False")
# 12. Python tuple program to add a list in the tuple
# list1 = [12,67]
# tup = (6,8,4)
# result = tuple(list(tup) + list1)
# print(result)
# 13. Python tuple program to find sum of elements in a tuple.
# tup = (4,6,2)
# print("Sum of elements in the tuple: ",sum(tup))
# 14.Python tuple program to create a tuple having squares of the elements from the list.
# tup = (1,3,5,7,6)
# print("Origianl tuple: ",tup)
# a = list()
# for i in list(tup):
#     b = i**2
#     a.append(b)
# tup = tuple(a)
# print("After sqauring elements: ",tup)
# 15. Python tuple program to multiply adjacent elements of a tuple.
# tup =  (1,2,3,4)
# list1 = []
# for a,b in zip(tup,tup[1:]):
#     c = a*b
#     list1.append(c)
# tup = tuple(list1)
# print("Multiplying adjacent elements: ",tup)
# 16. Python tuple program to convert a list into a tuple and multiply each element by 2.
# list1 = [12,65,34,77]
# list2 = []
# for ele in list1:
#     a = 2*ele
#     list2.append(a)
#
# tup = tuple(list2)
# print("Origianl list: ",list1)
# print("After multiplyting by 2: ",tup)
# 17. Python tuple program to remove an item from a tuple
# tup = ('p','y','t','h','o','n')
# print("Original tuple: ",tup)
# l = list(tup)
# l.remove('h')
# tup = tuple(l)
# print("After removing an element: ",tup)
# 18.Python tuple program to slice a tuple.
# tup = (5,7,3,4,9,0,2)
# print("Original tuple: ",tup)
# print(tup[:3])
# print(tup[2:5])
# 19.Python tuple program to find an index of an element in a tuple
# tup = ('s','q','a','t','o','o','l','s')
# print("Index of a: ",tup.index('a'))
# 20.Python tuple program to find the length of a tuple.
# tup = ('v','i','r','a','t')
# print("Original tuple: ",tup)
# print("Length of the tuple: ",len(tup))