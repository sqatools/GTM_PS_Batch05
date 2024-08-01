# Write a python program to find out all values which are prime in the given tuple values
# tup1 = (4, 7, 1, 8, 21, 23, 29)
# output = [7, 23, 29]

tup1 = (4, 7, 1, 8, 21, 23, 29)
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
