######################1)
#1) write a python program to print triangle pattern
"""
*
* *
* * *
* * * *
* * * * *
"""
for i in range(6):
    for j in range(i):
        print("*", end=" ")
    print()

print("-"*50)

#2)# write python program to print character triangle pattern
ascii = 65
for i in range(1, 6):
    for j in range(i):
        print(chr(ascii), end=" ")
        ascii += 1
    print()

print("-"*50)

#3)Tree pattern:

for i in range(1, 4):
    for j in range(1, 10):
        print("*", end=" ")
    print()

for i in range(1, 6):
    for j in range(1, 10):
        if j >3 and j < 7:
            print("*", end=" ")
        else:
             print(" ", end=" ")
    print()


print("-"*50)

#4)Python Loops program to print all alphabets from a to z using for loop
'''     Take chr method help to print characters with ASCII values
        chr(65) = ‘A’
        A-Z ASCII Range  65-90
        a-z ASCII Range  97-122'''

import string
print("Alphabet from a-z:")
for letter in string.ascii_lowercase:
    print(letter, end =" ")

print("\nAlphabet from A-Z:")
for letter in string.ascii_uppercase:
    print(letter, end =" ")

print("-"*50)

''''##5)Python Loops program to construct the following pattern, using a nested for loops.
Output :
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
for i in range(6):
    print(i*"*")
for i in range(4, -1, -1):
        print(i * "*")

print("-"*50)

'''6)Write a  Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
Input1:1500
Input2:2700
'''
for i in range(1500,2701):
    if i%7 == 0 and i%5 == 0:
        print(i)

print("-"*50)

'''7) Python Loops program that will add the word from the user to the empty string using python.
Input: “python”
Output : “python”
'''
word ="python"
string = ""
for i in range(len(word)):
    #print(word)
    string += word[i]

print(string)

print("-"*50)

'''8)Python Loops program to count the number of even and odd numbers from a series of numbers using python.
Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
Output :
Number of even numbers: 4
Number of odd numbers: 5
'''
Input = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for val in Input:
     if val%2 == 0:
         even += 1
     else:
         odd += 1

print("Number of even numbers:", even)
print("Number of even numbers:", odd)

print("-"*50)

##9)Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
for i in range(0,7):
    if i !=3 and i !=6:
        print(i, end=" ")

print("-" * 50)

##10)Write a program to get the Fibonacci series between 0 to 20 using python.
#Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181

n1 = 0
n2 = 1
count = 0

while count < 20:
    print(n1, end=" ")
    A = n1 + n2
    n1 = n2
    n2 = A
    count += 1

print("-" * 50)
print("-" * 50)

'''11) Write a program that iterates the integers from 1 to 30 using python.
 For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
For numbers that are multiples of both three and five print “FizzBuzz”. '''

for i in range(1,31):
    if i%3 ==0:
        print(i,":Fizz")
    elif i%5 ==0:
            print(i,":Buzz")
    elif i%3 ==0 and i%5 ==0:
        print(i,":FizzBuzz")

print("-" * 50)
'''12) Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using  python.
Input : “SqaTOOlS”
Output : “sqatools”'''

#word = input("Enter word: ")
word = "SqaTOOls"
result = ''
for char in word:
    if char.isupper():
        print(char.lower(),end="")
    else:
        print(char,end="")

print("-" * 50)

#str1 = input("Enter input string:")
str1 = "SqatoolS"
result = ""
for char in str1:
    char_ascii = ord(char)
    if 65 <= char_ascii <= 90:
        char_position = char_ascii - 65
        result = result + chr(97+char_position)
    else:
        result = result + char

print("Result :", result)

print("-" * 50)

''''##13) loops program that accepts a string and calculates the number of digits and letters using python.
Input : “python1234”
Output :
Letters 6
Digits 4 
'''
Input = "python1234"
letter = 0
Digit = 0

for i in Input:
    if i.isalpha():
        letter +=1
    elif i.isnumeric():
        Digit +=1

print("Letter:", letter)
print("Digit:", Digit)
print("-" * 50)
####14)Python Loops program to print all natural numbers from 1 to n using a while loop in python.
n=5
#n = int(input("Enter the last number: "))
count = 1

while count <= n:
    print(count,end=" ")
    count += 1
print("-" * 50)

####15) Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.
#n = int(input("Enter the number:"))
n=5
count = n

while count != 0:
    print(count,end =" ")
    count -=1
print("-" * 50)
print("-" * 50)
''''#16)Python Loops program to print all alphabets from a to z using for loop
        Take chr method help to print characters with ASCII values
        chr(65) = ‘A’
        A-Z ASCII Range  65-90
        a-z ASCII Range  97-122
        '''
count = 65
for _ in range(26):
    print(chr(count), end=" ")
    count += 1
print()

count = 97
for _ in range(26):
    print(chr(count), end=" ")
    count += 1

print()
print("-" * 50)

####16) Loops program to print all even numbers between 1 to 100 in python.

for i in range(1,101):
    if i%2 == 0:
        print( i, end=" ")

print("-" * 50)
print("-" * 50)
####17)Python Loops program to print all odd numbers between 1 to 100 using python.

for i in range(1,101):
    if i%2 != 0:
        print( i,end=" ")

print("-" * 50)
print("-" * 50)

####18)Python Loops program to find the sum of all natural numbers between 1 to n using python.
#n = int(input("Enter a number:"))
n =6
sum =0

for i in range(1,n+1):
    sum +=i

print(sum)

print("-" * 50)

###19)Python program to find the sum of all even numbers between 1 to n using
#Even
n =6
sum =0

for i in range(1,n+1):
    if i%2 == 0:
        sum +=i

print(sum)

print("-" * 50)
#Odd:

n =6
sum =0

for i in range(1,n+1):
    if i%2 != 0:
        sum +=i

print(sum)

print("-" * 50)

##20)Write a program to count the number of digits in a number using
#num = int(input("Enter a number:"))
num = '5373992'
count = 0

for i in num:
    count += 1

print(num,count)

print("-" * 50)







