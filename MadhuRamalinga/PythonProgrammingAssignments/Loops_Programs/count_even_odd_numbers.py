# Count the number of even and odd numbers

numbers = (1, 2, 4, 5, 8, 10, 15, 18, 21, 25)
even = 0
odd = 0
for val in numbers:
    if val%2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Even numbers are: ", even)
print("Odd numbers are: ", odd)

