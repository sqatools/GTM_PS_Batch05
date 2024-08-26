# Python: How to Read a File in Reading Mode

def read_file(filename):
    file = open(filename, "r")
    file_data = file.read()
    print(file_data) # Test file for filehandling
    file.close()

read_file("read_test_file")