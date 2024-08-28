# Python file program to count all the words from a file

open_file = open("read_test_file")
words = open_file.read().split()

count = 0

for word in words:
    count += 1

print("Count of all words:", count) # 39