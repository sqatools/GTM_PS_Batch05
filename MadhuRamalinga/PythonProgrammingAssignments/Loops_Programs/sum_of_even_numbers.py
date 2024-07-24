# Find the sum of even numbers between 1 to n
num = int(input("Enter the number: "))
count = 0
for i in range(1,num+1):
    if i%2 == 0:
        count += i
print("Sum of even numbers is:",count)