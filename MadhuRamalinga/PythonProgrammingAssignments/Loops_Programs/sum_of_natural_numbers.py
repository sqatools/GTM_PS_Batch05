# Find the sum of natural numbers between 1-n
num = int(input("Enter the last number: "))
total = 0

for i in range(1,num+1):
    total += i

print(total)