# Program that take a number as a parameter and checks whether the number is prime or not

def prime(num1):
    for i in range(2, n):
        if n%i == 0:
            prime = False
        else:
            prime = True

    if prime:
        print("This is prime number :", n)
    else:
        print("This is not prime number:", n)

n = int(input("Enter the number: "))
prime(n)

# Enter the number: 5
# This is prime number : 5