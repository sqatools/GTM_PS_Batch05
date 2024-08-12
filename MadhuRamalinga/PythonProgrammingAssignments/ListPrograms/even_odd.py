# Program to differentiate even and odd elements from a list

list1 = [1, 3, 4, 5, 8, 10]

for val in list1:
    if val % 2 == 0:
        print(f"{val} is a even number")
    else:
        print(f"{val} is a odd number")

# 1 is a odd number
# 3 is a odd number
# 4 is a even number
# 5 is a odd number
# 8 is a even number
# 10 is a even number

###### OR ########
print("_"*50)

list1 = [1, 3, 4, 5, 8, 10]
even = []
odd = []

for val in list1:
    if val % 2 == 0:
        even.append(val)
    else:
        odd.append(val)

print("Even numbers are: ", even)
print("Odd numbers are: ", odd)

# Even numbers are:  [4, 8, 10]
# Odd numbers are:  [1, 3, 5]