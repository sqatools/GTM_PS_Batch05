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

print("Alphabet from A-Z:")
for letter in string.ascii_uppercase:
    print(letter, end =" ")

print("-"*50)