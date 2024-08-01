# Get all the palindrome words from the string

str1 = "malayalam is a language"
list1 = str1.split()
new_list = []

for val in list1:
    if val == val[::-1]:
        new_list.append(val)
print(new_list)        