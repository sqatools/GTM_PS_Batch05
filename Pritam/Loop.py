# 1 . program to find those numbers which are divisible by 7 and multiple of 5
# for i in range(1500,2701):
#         if i%7 == 0 and i%5 == 0:
#             print(i, end=" ")

# 2. program to count the number of even and odd numbers from a series of numbers

# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# even = 0
# odd = 0
#
# for val in numbers:
#     if val%2 == 0:
#         even += 1
#     else:
#         odd += 1
#
# print("Number of even numbers: ",even)
# print("Number of odd numbers: ",odd)

# 3,  program that prints all the numbers from 0 to 6 except 3 and 6

# for i in range(0,11):
#         if i != 3 or i != 6:
#             print(i,end=" ")

# 4.  program that accepts a string and calculates the number of digits and letters
# word = "python1234"
# digit = 0
# character = 0
#
# for ele in word:
#     if ele.isalpha():
#         character += 1
#     elif ele.isnumeric():
#         digit += 1
#
# print("Digits :",digit)
# print("Characters: ",character)

# # 5.  program to print all natural numbers from 1 to n using a while loop
# n = int(input("Enter the last number: "))
# count = 1
#
# while count <= n:
#     print(count,end=" ")
#     count += 1
# 6.  program to print all natural numbers in reverse (from n to 1) using a while loop
# n = int(input("Enter the last number: "))
# count = n
#
# while count != 0:
#     print(count,end=" ")
#     count -= 1

# 7.program to print all even numbers between 1 to 100
# for i in range(1,101):
#     if i%2 == 0:
#         print(i,end=" ")
# # 8.  program to print all odd numbers between 1 to 100
# for i in range(1,101):
#     if i%2 != 0:
#         print(i,end=" ")

# 9. program to find the sum of all natural numbers between 1 to n
# n= int(input("Enter the last number: "))
# total = 0
#
# for i in range(1,n+1):
#     total += i
#
# print(total)

# 10.  program to find the sum of all odd numbers between 1 to n
# n= int(input("Enter the last number: "))
# total = 0
#
# for i in range(1,n+1):
#     if i%2 != 0:
#         total += i
#
# print(total)

# 11. program to enter a number and print it in words.
# num = int(input("Enter a number: "))
# str1 = ""
#
# for i in str(num):
#     if i == "1":
#         str1 += "One"
#     elif i == "2":
#         str1 += "Two"
#     elif i == "3":
#         str1 += "Three"
#     elif i == "4":
#         str1 += "Four"
#     elif i == "5":
#         str1 += "Five"
#     elif i == "6":
#         str1 += "Six"
#     elif i == "7":
#         str1 += "Seven"
#     elif i == "8":
#         str1 += "Eight"
#     elif i == "9":
#         str1 += "Nine"
#
# print(str1)

# 12  program to print all Perfect numbers between 1 to n
# num = int(input("Enter a number: "))
#
# for i in range(1,num):
#     total = 0
#     for j in range(1,i):
#         if i % j == 0:
#             total += j
#     if total == i:
#        print(i, end=' ')

# 13.  program to print the multiplication table of any number
# num = int(input("enter num="))
# a = 0
#
# for i in range(1,11):
#     a = i*num
#     print(i,"*",num,"=",a)

# 14. program to print the pattern T using Python Loops
# for i in range(2):
#     for j in range(9):
#         print("*", end="")
#     print()
#
# for i in range(5):
#     for j in range(9):
#         if j> 2 and j <6:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# 15.  program to get input from the user if it is a number insert it into an empty list
# data = "125python"
# List = []
#
# for char in data:
#     if char.isnumeric():
#         List.append(int(char))
#
# print(List)

# 16. program to construct the following pattern,
# for i in range(6):
#     print(i*"*")
# 17 . program to construct the following pattern
# for i in range(6,0,-1):
#     print(i*"*")
# 18.  program to construct the following pattern, using a nested for loop
# for i in range(1,6):
#         for j in range(i):
#             print(i,end=" ")
#         print()
# 19.  program to print the following pattern
# for i in range(6):
#     print(i*"*")
# for i in range(6,0,-1):
#     print(i*"*")
# 20. program to print each word in a string on a new line
# str1 = "Sqatools"
#
# for char in str1:
#     print(char,end="\n")