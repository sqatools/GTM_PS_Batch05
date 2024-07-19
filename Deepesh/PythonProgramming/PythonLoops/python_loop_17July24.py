# write a python program to print values from 1 to 10
# range(start value, end value, difference)
for i in range(1, 20, 3):
    print(i, end=" ")

print()
print("_"*50)
for j in range(10, 0, -1):
    print(j, end=" ")


print("_"*50)
# combine if with for loop
for k in range(1, 50, 1):
    if k%2 == 0:
        print(k)

# use range with default initial value and different
# default initial value is 0
# default difference is 1
print("_"*50)

for i in range(8):  # initial value is zero, and difference is 1
    print(i, end=" ")
# 0 1 2 3 4 5 6 7

print()
for j in range(2, 8): # default difference is 1
    print(j, end=" ")
# 2 3 4 5 6 7

print()
print("_"*50)
###############################
# Apply loop on string and repeat the specific char twice
str1 = "Programming"

for char in str1:
    #print(char)
    if char == 'g':
        print(char*2)
    else:
        print(char)


# write a python program to print square of even value and cube of odd values in list
print("_"*40)
list1 = [4, 6, 7, 2, 5, 3]
for val in list1:
    #print(val)
    if val%2 == 0:
        print(val, val**2)
    else:
        print(val, val**3)


# write a python program to read key and value from dictionary
print("_"*50)
dict1 = {'a': 123, 'b': 345, 'c': 678}
for data in dict1.items():
    print(data)


for key, value in dict1.items():
    print("key :", key, "value:", value)

###########################################
#1 write a python program print all value which are divisible by and 3 and 5 from given list
list2 = [3, 9, 15, 30, 45, 16, 25]

#2 write a python program to get print all the vowels from given string.
str_a = "Python Programming"
vowels = "aeiouAEIOU"

for char in str_a:
    if char in vowels:
        print(char)

#################### Nested For LOOP Condition ############################
print("_"*50)

for i in range(1, 6):# 1, 2, 3, 4, 5
    print("Address :", i)
    for j in range(1, 4): # 1, 2, 3
        print("Package :", j)
    print("_"*20)


"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

for i in range(0,5):# 0, 1, 2, 3, 4
    for j in range(0, 5):# 0-4
        print("*",end=" ")
    print()

print("_"*50)
# write a python program to print triangle pattern
"""
*
* *
* * *
* * * *
* * * * *
"""

for i in range(6):
    for j in range(i):
        print("*", end=" ")
    print()
