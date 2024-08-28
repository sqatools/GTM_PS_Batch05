# Python file program to read a random line from a file

import random # Import random library

open_file = open('read_test_file').read().splitlines() # Read data from the file and splitting it into lines

data = random.choice(open_file) # Get a random line from the lines

print(data) # Line6 : abc
