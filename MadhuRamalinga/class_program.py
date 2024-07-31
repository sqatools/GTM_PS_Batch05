
#1 write a python program print all value which are divisible by and 3 and 5 from given list
list2 = [3, 9, 15, 30, 45, 16, 25]
for val in list2:
    if val%3 == 0:
        print(val, end=" ")
    if val%5 == 0:
        print(val, end=" ")
print()
print("_"*50)

#2 write a python program to get print all the vowels from given string.

str_a = "Python Programming"
vowels = "aeiouAEIOU"
for char in str_a:
    if char in vowels:
        print(char)