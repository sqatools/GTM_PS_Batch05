# Python program to get a specific line from the file

open_file = open("read_test_file","r")
read_file = open_file.readlines()

print("First line is -", read_file[0]) # First line is - Line1 : Test file for filehandling
open_file.close()
