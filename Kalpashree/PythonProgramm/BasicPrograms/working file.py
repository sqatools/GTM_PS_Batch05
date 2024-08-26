#Q1 : Write a python program to find out all values which are prime in the given tuple values
tup1 = (4, 7, 1, 8, 21, 23, 29)
output = [7, 23, 29]

for num in range(len(tup1)):
    for i in range(2, num):
        if num % i == 0:
            break
        else:
            print(num)
            break


# Q2 : Write a python program to factorial of given values
num =5
# fact 5: 5*4*3*2*1 = 120
#output = [24, 120, 6, 729]
factorial = 1
if num >= 1:
    for i in range (1, n+1):
        factorial=factorial *i
print("Factorial of the given number is: ", factorial)