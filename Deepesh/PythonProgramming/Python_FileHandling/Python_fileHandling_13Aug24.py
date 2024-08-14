"""
# Different file modes.
read mode (r) :
write mode (w) :
append mode (a) :
"""

def read_file_data(filename):
    file = open(filename, "r")
    file_data = file.read()
    print(file_data)
    file.close()

#read_file_data("test_data_read.txt")
#read_file_data("E:\\Filesdata\\count_name.txt")

# open file in write mode

def write_content_to_file(filename, content):
    file = open(filename, "w")
    file.write(content)
    file.close()

# CASE 1: Open a non existing file with write mode : In this case write mode will create
#          fresh file with the provided name, then update the file content
# write_content_to_file("write_content.txt", "Adding content the file")

# CASE 2: Open a existing file with write a mode : In this case write mode will over write the
#        existing content of the file and update it.
# write_content_to_file("write_existing_file.txt", "Adding new content to the file")
