# Program to copy the file’s contents to another file after converting it to lowercase

with open('read_test_file','r') as data_file:
    with open('writecontent.txt','a') as output_file:
        for line in data_file:
            output_file.write(line.lower())