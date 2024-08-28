# Program to count the number of lines in a file

file = open('read_file2','r')
lines = file.readlines()
count = 0

for line in lines:
    count += 1
print("Total number of lines in read_file2:", count) # Total number of lines in read_file2: 8