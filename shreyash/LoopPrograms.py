#Find numbers divisible by a certain number
# Write a  Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
#for i in range(1500,2701):
#        if i%7 == 0 and i%5 == 0:
#            print(i, end=" ")

#Q2:Python Loops program to construct the following pattern, using a nested for loops
#for i in range(6):
#    print(i*"*")
#for i in range(4,-1,-1):
#    print(i*"*")

#Q3:Python Loops program that will add the word from the user to the empty string using
#word = input("Enter the word: ")
#str1 = ""
#for i in range(len(word)):
#    str1 += word[i]

#print(str1)

#Q4: Write a program that iterates the integers from 1 to 30 using python. For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
#For numbers that are multiples of both three and five print “FizzBuzz”.

#for i in range(1,31):
#    if i%3 == 0 and i%5 == 0:
#        print("FizzBuzz")
#    elif i%3 == 0:
#        print("Fizz")
#    elif i%5 == 0:
#        print("Buzz")


#Q5:Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using python.

#input1 = input("Enter word: ")
#result = ''
#for char in input1:
#    if char.isupper():
#        print(char.lower(),end="")
#    else:
#        print(char,end="")

#Q6:Python loops program that accepts a string and calculates the number of digits and letters using python.
#word = "python1234"
#digit = 0
#character = 0

#for ele in word:
#    if ele.isalpha():
#        character += 1
#    elif ele.isnumeric():
#        digit += 1

#print("Digits :",digit)
#print("Characters: ",character)

#Q7: Python Loops program to print all natural numbers from 1 to n using a while loop in python.

#n = int(input("Enter the last number: "))
#ount = 1

#while count <= n:
#    print(count,end=" ")
#    count += 1

#Q8:Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.

#n = int(input("Enter the last number: "))
#count = n

#while count != 0:
#    print(count,end=" ")
#    count -= 1

#Q9:Python Loops program to print all alphabets from a to z using for loop
#        Take chr method help to print characters with ASCII values
#       chr(65) = ‘A’

#import string

#print("Alphabet from a-z:")
#for letter in string.ascii_lowercase:
#    print(letter, end =" ")

#print("\nAlphabet from A-Z:")
#for letter in string.ascii_uppercase:
#    print(letter, end =" ")

#Q10: Python Loops program to print all even numbers between 1 to 100 in python.

#for i in range(1,101):
#    if i%2 == 0:
#        print(i,end=" ")

#Q11:Loops program to print all odd numbers between 1 to 100 using python.

#for i in range(1,101):
#    if i%2 != 0:
#        print(i,end=" ")

#Q12:Write a program to find the first and last digits of a number using python.

#num = 2665
#str1 = str(num)

#for i in range(len(str1)):
#    if i == 0:
#        print("First number in the gievn number : ",str1[i])
#    elif i == len(str1)-1:
#        print("Last number in the gievn number : ",str1[i])

#Q13:Write a program to find the sum of the first and last digits of a number using python.
#num = 2665
#str1 = str(num)
#total= 0

#for i in range(len(str1)):
#    if i == 0:
#        total += int(str1[i])
#    elif i == len(str1)-1:
#        total += int(str1[i])

#print("Sum of first and last number: ",total)

#Q14: Python loops program to enter a number and print its reverse using python.

#n = int(input("Enter a number: "))
#rev = 0

#while n>0:
#    r = n%10
#    rev = (rev*10) + r
#    n = n // 10

#print("Reverse number: ",rev)

#Q15:Find the frequency of each digit in a number
#num = 12312543
#str1 = str(num)
#dict1 = {}

#for val in str1:
#    if val in dict1:
#       dict1[val] += 1:
#    else:
#       dict1[val] = 1:
#print(dict1)
