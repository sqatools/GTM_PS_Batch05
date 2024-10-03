# 1. Get a string made of first and the last 2 chars
# string = "sqatools"
#
# if len(string) < 2:
#     print(True)
# else:
#     print(string[:2]+string[-2:])

# 2.  string program that takes a list of strings and returns the length of the longest string
# string = ["i", "am", "learning", "python"]
# temp = 0
#
# for word in string:
#     a = len(word)
#     if a > temp:
#         temp = a
#
#
# print(temp)

# 3. string program to get a string made of 4 copies of the last two characters of a
# specified string (length must be at least 2).
# string = "Sqatools"
#
#
# print(string[-2:]*4)
# 4. string program to reverse a string if it’s length is a multiple of 4.
# string = "sqatools"
#
# if len(string) % 4 == 0:
#     print(string[::-1])

# 5. string program to count occurrences of a substring in a string

# string = "sqatoolspythonspy"
# sub = "spy"
#
#
# string.count("spy")

# 6. string program to test whether a passed letter is a vowel or consonant.
# letter = "aerv"
#
# for char in letter:
#     if char == "a" or char =="e" or char =="i"
#     or char =="o" or char =="u":
#         print(f"{char} is vowel")
#     else:
#         print(f"{char} is consonant")

# # 7. Find the longest and smallest word in the input string.
# string = "we are learning python"
# list1 = string.split(" ")
#
# print("Longest word: ", max(list1, key = len))
# print("Smallest word: ", min(list1, key = len))

# 8.  Print most simultaneously repeated characters in the input string.
# str1 = "Helllllo ffdfdas sdfsfsd sssfdddd"
# max_repeat_count = 0
# max_repeat_char = ''
#
# temp = 1
# for i in range(len(str1)-1):
#     if str1[i] == str1[i+1]:
#         temp = temp + 1
#         if temp > max_repeat_count:
#             max_repeat_count = temp
#             max_repeat_char = str1[i]
#     else:
#         temp = 1
#
# print("Max repeated char :", max_repeat_char,
#       "\nMax repeated count :", max_repeat_count)

# 9. Python program to calculate the length of a string with loop logic
# string = "im am learing python"
# count = 0
#
# for char in string:
#     count +=1
#
# print("Length of the string using loop logic: ", count)
# print("Length of the string using len(): ", len(string))

# 10.  program to get to swap the last character of a given string.
# string = "SqaTool"
# print(string[-1]+string[1:-1]+string[0])

# 11. program to exchange the first and last character of each word from the given string.
# string ="Its Online Learning"
#

# list1 = string.split(" ")
#
# for word in list1:
#     new_word = word[-1]+word[1:-1]+word[0]
#     index = list1.index(word)
#     list1[index] = new_word
#
# print(" ".join(list1))

# 12. count vowels from each word in the given string show as dictionary output.
# string= "We are Learning Python Codding"
# list1 = string.split(" ")
# vowels = "aeiou"
# dictionary = dict()
#
# for word in list1:
#     count = 0
#     for char in word:
#         if char in vowels:
#             count +=1
#     dictionary[word] = count
# print(dictionary)

# 13. python to repeat vowels 3 times and consonants 2 times
# str1  = "Sqa Tools Learning"
# result = ""
# vowels = ["a","e","i","o","u",
#           "A","E","I","O","U"]
#
# for char in str1:
#     if char in vowels:
#         result = result + char*3
#     else:
#         result = result + char*2
# print(result)

# 14. python program to replace the words “Java” with “Python” in the given string.
# string = "JAVA is the Best Programming Language in the Market"
# List1 = string.split(" ")
#
# for word in List1:
#     if word == "JAVA":
#         index = List1.index(word)
#         List1[index] = "PYTHON"
#
# #Printing output
# print(" ".join(List1))

# # 15. Python program to create a string with a given list of words
# list1 = ["There", "are", "Many", "Programming", "Language"]
# print(" ".join(list1))