# Most simultaneously repeated character in string

str1 = "Hellllo Welcomeeeee to Python Programmmming"
highest_count = 0
highest_repeat_char = ''

temp = 1
for i in range(len(str1)-1):
    if str1[i] == str1[i+1]:
        temp = temp + 1
        if temp > highest_count:
            highest_count = temp
            highest_repeat_char = str1[i]
    else:
        temp = 1

print("The most repeated character in the given string is:", highest_repeat_char, "\n The count is:", highest_count)



