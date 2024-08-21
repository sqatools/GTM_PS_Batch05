# Program to get the file’s first three and last three lines

open_file = open("read_test_file","r")
read_file = open_file.readlines()

for val in (read_file[:3]):
    print(val)

for val in (read_file[-3:]):
    print(val)

# Line1 : Test file for filehandling
#
# Line2 : ABC
#
# Line3 : XYZ
#
# Line8 : alpha
#
# Line9 : Beta
#
# Line10: Gamma