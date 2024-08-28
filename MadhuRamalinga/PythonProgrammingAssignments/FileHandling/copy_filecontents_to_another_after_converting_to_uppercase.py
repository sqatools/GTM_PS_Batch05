# Copy the file’s contents after converting it to uppercase

with open('read_test_file','r') as file:
    with open('write_test_file','a') as output_file:

        for line in file:
            output_file.write(line.upper())