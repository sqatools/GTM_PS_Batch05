# Q1 : Write a python program to change reverse each values in given list
# list2 = ['Hello', 'Python', 'Programs']
# output = ['olleH', 'nohtyP', 'smargorP']

list2 = ['Hello', 'Python', 'Programs']
reverse_value = []
for char in list2:
    reverse_value.append(char[::-1])
print("Reverse of each value is: ",reverse_value)

# using list comprehension

reverse_value = [char[::-1] for char in list2]
print("Reverse of each value is: ",reverse_value)

