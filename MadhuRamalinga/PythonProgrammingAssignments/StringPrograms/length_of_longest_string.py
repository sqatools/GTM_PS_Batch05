# From list of strings, length of longest string

str1 = ["I", "Love", "Python", "Programming"]
string_length = 0
for char in str1:
    if len(char) > string_length:
        string_length = len(char)

print("The length of the longest string is: ", string_length) # The length of the longest string is:  11
