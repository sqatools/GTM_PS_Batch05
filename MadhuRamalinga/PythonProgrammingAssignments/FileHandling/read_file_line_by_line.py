# Program to read a file line by line and store it in a list

result_list = []

with open("read_test_file", "r") as file: # Read file with context manager
    while True:
        line = file.readline() # read all line one by one until it is blank
        if not line: # once receive blank line, then break the loop

            break
        result_list.append(line)

    print(result_list)

# ['Line1 : Test file for filehandling\n', 'Line2 : ABC@gmail.com of Line2\n', 'Line3 : XYZ\n', 'Line4 : 123\n', 'Line5 : 456@yahoo.com of Line5\n', 'Line6 : abc\n', 'Line7 : xyz\n', 'Line8 : alpha\n', 'Line9 : Beta@outlook.com of Line9\n', 'Line10: Gamma']
