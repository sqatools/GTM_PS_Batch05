# Python program to create a dictionary from the string.

str1 = 'Python Programming'
dict1 = {}

for char in str1:
    dict1[char] = str1.count(char)

print(dict1) # {'P': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, ' ': 1, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 1}