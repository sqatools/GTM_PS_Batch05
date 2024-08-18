"""
# Different file modes.
read mode (r) : Open file in read mode allow us to read all the data of the file.
write mode (w) : When open file in write mode and write some content in the file, it will
                 overwrite the existing content.
append mode (a) : When we open a file in append mode and write content in the file, then
                  it will append content at the end of the file.
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

########## Open file in append mode ########

def append_content_to_file(filename, content):
    file = open(filename, "a")
    file.write(content)
    file.close()


# Case1 : append content to existing file
#content = "\n Appending fresh content to the file"
#append_content_to_file("append_content_to_file.txt", content)

# Case 2:  append content to file that doest not exist: It will create new file and add content to
#          it
"""
content = "\nHello Good Morning, Hope you are doing good"
append_content_to_file("append_content_fresh.txt", content)
append_content_to_file("E:\\Filesdata\\batch05\\append_content_fresh.txt", content)
"""

# context manager : It open file and close automatically no need to close the file explicitly.
# content manager has its own enter and exist method.

def read_content_with_context(filename):
    with open(filename, "r") as file:
        data = file.read()
        print(data)
        print("check file is closed inside context manager:", file.closed) # False

    print("check file is closed outside context manager:", file.closed) # True

#read_content_with_context("test_data_read.txt")

print("_"*50)
#################################
# different option to read file
# 1. read number of line with readline() method
# 2. read number of characters with read(byte) method
# 3. read list of all the lines in the file with readlines() method

# 1. read number of line with readline() method

def read_specific_lines(filename, line_no):
    with open(filename, "r") as file:
        for _ in range(line_no):
            data = file.readline()
            print(data, end="")


#read_specific_lines("test_data_read.txt", 3)

# 2. read number of characters with read(byte) method

def read_number_of_characters(filename, no_byte):
    with open(filename, "r") as file:
        data = file.read(no_byte)
        print(data)


# read_number_of_characters("test_data_read.txt", 20)

# 3. read list of all the lines in the file with readlines() method
def read_list_of_lines(filename):
    with open(filename, "r") as file:
        lines_list = file.readlines()
        print(lines_list)
        return lines_list

list_lines = read_list_of_lines("test_data_read.txt")

# read last three lines
for i in range(-3, 0, 1):
    print(list_lines[i], end="")

"""
7. AI revolutionizes digital interaction
8. and task automation, offering a suite
9. of no-code apps and automation...
"""

# read first three lines
for j in range(3):
    print(list_lines[j], end="")

"""
1. What is Thunderbit AI?
2. Thunderbit AI revolutionizes digital interaction
3. and task automation,
"""


# tell() method : Tell method return the current position of the cursor
# seek() method : seek method helps to set cursor position on different level, like, begining of file, end of the file, or
#                 current position of the cursor.

def update_file_content_with_append_mode(filename):
    with open(filename, "ab+") as file:
        print("position of the cursor :", file.tell())
        file.seek(0, 0)
        print("position of the cursor :", file.tell())
        new_content = b"adding message in begining of file\n"
        print(file.read(10))
        file.seek(20, 1)  # set cursor from current location of cursor
        #file.write(new_content)
        print("position of the cursor :", file.tell())
        file.seek(-30, 2) #
        print(file.read())

update_file_content_with_append_mode("test_data_read.txt")
