# Python file program to overwrite the existing file content

def write_to_file(filename, contents):
    file = open(filename, "w")
    file_data = file.write(contents) # ABC
    file.close()

write_to_file("write_test_file", "ABC")

########## OR ###########
print("_"*50)

file1 = open("writecontent.txt","w")
# write new content to the file
file1.write("New Line : This is china") # New Line : This is china
# close the file
file1.close()