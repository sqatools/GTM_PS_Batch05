# Replace the second occurrence of a character

str1 = 'Programming'
result = ''

for char in str1:
    if char in result:
        result += '$'
    else:
        result += char
print("Result:", result)