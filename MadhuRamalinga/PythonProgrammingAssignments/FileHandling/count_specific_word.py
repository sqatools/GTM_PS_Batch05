# Program to count of a specific word in a file

open_file = open('read_test_file','r')

words = open_file.read().split() # Read the data in the file and convert it into words

count = 0

for word in words:
    if word == 'Python':
        count += 1

print("Count of Python in the file:", count)