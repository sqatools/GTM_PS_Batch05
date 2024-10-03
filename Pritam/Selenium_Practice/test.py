#1.Print each character on new line
# str1 = "python"
#
# for char in str1:
#     print(char, end="\n")
# 2. Print the given string 3 times
# str1 = "Sqatools"
# print(str1*3)

# 3. The reverse words in a string
# str1 = "String Problem"
# print(" ".join(reversed(str1.split(" "))))
# 4. Extract the name from the email address
# str1 = "student@gmail.com"
# index = str1.index("@")
# str2 = ""
# for char in str1[:index]:
#     if char.isalpha():
#         str2+= char
#         print(str2)
# 5. Remove unwanted char from string
# string = "sqa****too^^{ls"
# unwanted = ["#", "*", "!", "^", "%","{","}"]
#
# for char in unwanted:
#     string = string.replace(char,"")
# print(string)

# 6.Remove all characters except given character
# str1 = "Sqatools python"
#
# print(''.join([el for el in str1 if el == "S"]))
# 7.Find the maximum length of consecutive 0’s.
# string ="10001100000111"
# List1 = string.split("1")
# max = (max(List1,key=len))
# print(len(max))
# 8.Calculate the sum of digits in a given string.
# string = "12sqatools78"
# total = 0
# for char in string:
#     if char .isnumeric():
#         total+= int(char)
#         print("Sum",total)

# 9.Remove spaces from a given string
# string1 = "python at sqatools"
# str1 = ""
# for char in string1:
#     if char != " ":
#         str1 += char
#         print(str1)
# 10. Reverse the words in a string
# str1 ="sqatools python"
#
# print(" ".join(str1.split(" ")[::1]))
# print(str1[::-1])
# 11 calculate length of string
# str1 = "python learning is good"
# print(len(str1))
# 12 Remove empty spaces from a list of strings
# List1 =  ["Python", " ", " ","sqatools"]
# List2 = []
#
# for string in List1:
#     if string != " ":
#         List2.append(string)
# print(List2)
# 13 Find duplicate characters in a string

# string = "hello world"
# list1 = []
#
# for char in string:
#     if string.count(char) > 1:
#         list1.append(char)
#
# #Printing output
# print(set(list1))
# 14. Print the index of the character in a string.
# str1 = "Sqatools"
# # print("The index of q is: ", str1.index("q"))
# print("str1:", str1[3])
# 15 Count the vowels in a string
# string = "welcome to Sqatools"
# vowels = ["a","e","i","o","u"]
# count = 0
# for char in string:
#     if char in vowels:
#         count+= 1
# print(count)
# 16 Find the first repeated word in a given string.
#
# str1 = "ab bc ca ab bd ca"
# temp = []
#
# for word in str1.split():
#     if word in temp:
#         print("First repeated word: ", word)
#         break
#     else:
#         temp.append(word)
# str  = "India"
# print(str[-1])
# print(str[:-1])
# print(str[::-1])
# print(str[1])
# print(str[1:])
# print(str[1::])
# print(str[:3])
# print(str[::3])
# print(str[1::2])

# List1 = ["my","name"]
# List2 = ["is","john"]
# List3 = List1 +List2
# print(List3)
# List1.extend(List2)
# print(List1)
# print(' '.join(List1))

# combine 2 list and convert into dictionary
# List1 = ["a","b","c"]
# List2 = [1,2,3]
# dict1= dict(zip(List1,List2))
# print(dict1)

# class is called and count
# class A:
#     count = 0
#     def __init__(self):
#         A.count +=1
#         print("Class A  is called")
# a1 = A()
# a2 = A()
# print(A.count)
# Even number
# for i in range(1,101):
#     if i%2 == 0:
#         print(i,end=" ")
# odd number
# for i in range(1,101):
#     if i%2 !=0:
#         print(i,end=" ")













