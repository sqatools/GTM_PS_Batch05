# Find the first and last digits of a number.
num = '12345'
str1 = str(num)

for i in range(len(str1)):
    if i == 0:
        print("First digit in the given number is:",str1[i])
    elif i == len(str1)-1:
        print("Last digit in the given number is:",str1[i])