# Calculate the number of digits and letters
str1 = "Hello12345678"
digit = 0
char = 0
for val in str1:
    if val.isalpha():
        char += 1
    elif val.isnumeric():
        digit += 1
print("Digits: ",digit)
print("Characters: ", char)