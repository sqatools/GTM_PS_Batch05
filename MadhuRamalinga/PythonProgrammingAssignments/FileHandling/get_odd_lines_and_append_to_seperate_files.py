# Program to get odd lines from files and append them to separate files

open_file1 = open('read_test_file', 'r') # Open 1st file in read mode
open_file2 = open('writecontent.txt', 'w') # Open 2nd file in write mode

reading_lines = open_file1.readlines() # Read lines of the file

for val in range(0, len(reading_lines)): # Iterate over lines
    if(val % 2 != 0): # Check for odd line
        open_file2.write(reading_lines[val]) # Write lines to 2nd file
    else:
        pass

# Close the file
open_file1.close()
open_file2.close()
