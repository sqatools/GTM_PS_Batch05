#1.Find those numbers divisible by a certain number and a multiple of another number.for i in range(1500,2701):
for i in range(1500,2701):
        if i%7 == 0 and i%5 == 0:
            print(i, end=" ")

#2.Construct the following pattern.
        '''*
        * *
        * * *
        * * * *
        * * * * *
        * * * *
        * * *
        * *
        *'''
for i in range(6):
    print(i* "*")
for i in range(4,-1,-1):
    print("*" *i )

#3 Add the word in a string'''
print("_" *50)
word = input("Enter the word:")
str1 = ""
for i in range(len(word)):
    str1 += word[i]
print(str1)

#4 Count the number of even and odd numbers
print("_" *50)
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even=0
odd=0
for val in numbers:
    if val % 2 ==0:
        even += 1
    else:
        odd += 1
print("No. of even number:",even)
print("No.of odd numbers:",odd)

#5 Print all numbers except certain numbers.
print("_" *50)
for i in range(0,11):
    if i != 3 or i != 6:
        print(i,end= "_")

#6Get the Fibonacci series between 0 to 20.
print("_" *50)
num1 = 0
num2 = 1
count = 0
while count < 20:
    print(num1,end=" ")
    n2 = num1 + num2
    num1 = num2
    num2 = n2
    count += 1

#7 In this program, we will print Fizz Buzz and FizzBuzz for multiples of certain numbers.
print("_" *50)
for i in range(1,31):
    if i%3 == 0 and i%5 ==0:
        print("FIZZ BUZZ")
    elif i % 3 == 0:
        print("FIzz")

    elif i % 5 ==0:
        print("BUZZ")
#8Convert all uppercase to lowercase in a word
print("_" *50)
input1=input("Enter word")
result = ''
for i in input1:
    if(i.isupper()):
        print(i.lower(),end = "")
    else:
        print(i,end = "")

#9Print all natural numbers from 1 to n
n = int(input("Enter the last number: "))
count = 1

while count <= n:
    print(count,end=" ")
    count += 1
#10Print all natural numbers in reverse (n to 1)
n = int(input("Enter the last number: "))
count = n

while count != 0:
    print(count,end=" ")
    count -= 1