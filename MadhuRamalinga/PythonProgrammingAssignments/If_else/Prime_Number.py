# Program to check whether the number is a prime number.

count = 0
num = int(input("Enter the number: "))
for i in range(2,num):
    if num%i == 0:
        count = count + 1
    if count > 0:
        print("It is not a prime number")
    else:
        print("It is a prime number")

        