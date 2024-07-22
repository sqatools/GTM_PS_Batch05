# Python program to check whether the string is palindrome
str1 = input("Enter the string: ")
str2 = str1[::-1]
if str1 == str2:
    print("It is a palindrome")
else:
    print("It is not a palindrome")