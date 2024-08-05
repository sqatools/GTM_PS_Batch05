# Repeat vowels and consonants 3 and 2 times resp.

str1 = 'I like python programming'
result = ''
vowels = ["a","e","i","o","u","A","E","I","O","U"]

for char in str1:
    if char in vowels:
        result += char*3
    else:
        result += char*2
print(result)

