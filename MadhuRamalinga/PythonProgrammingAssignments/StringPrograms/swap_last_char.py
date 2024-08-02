# Swap the last character of a string

str1 = "Python"
str_list = list(str1) # ['P', 'y', 't', 'h', 'o', 'n']

str_list[0], str_list[-1] = str_list[-1], str_list[0]

swapped_str = "".join(str_list)
print("Swapped string is:", swapped_str)


####### OR ########

string = "SqaTool"

print(string[-1]+string[1:-1]+string[0]) # lqaTooS