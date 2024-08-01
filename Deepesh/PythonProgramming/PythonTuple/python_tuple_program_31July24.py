#Q1 : Write a python program to find out all values which are prime in the given tuple values
tup1 = (4, 7, 1, 8, 21, 23, 29)
#output = [7, 23, 29]

output = []
for n in tup1:
#n = 12
    prime = True
    for i in range(2, n):
        if n%i == 0:
            prime = False
            break
        else:
            continue

    if prime:
        print("This is prime number :", n)
        output.append(n)
    else:
        print("This is not prime number:", n)



print("Prime number list :", output)

print("_"*50)
# Q2 : Write a python program to factorial of given values
tup2 = (4, 5, 3, 7)
# fact 5: 5*4*3*2*1 = 120
#output = [24, 120, 6, 5040]
result = []

for n in tup2:
    fact = 1
    for i in range(n, 0, -1):
        fact = fact*i # 6 # 30 # 120 # 360 # 720

    result.append(fact)

print("output :", result)

