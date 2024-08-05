# Python program to check whether a number is palindrome
num1 = input("Enter the number: ")
num2 = num1[::-1]
if num1 == num2:
    print("It is a palindrome")
else:
    print("It is not a palindrome")