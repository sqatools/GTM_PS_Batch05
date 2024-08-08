# Get all the digits from the string

str1 = "123 Python 456 Programming 10"
list1 = str1.split()
list2 = []

for val in list1:
    if val.isnumeric():
    # if val.isdigit():
        list2.append(val)
print(list2) # ['123', '456', '10']