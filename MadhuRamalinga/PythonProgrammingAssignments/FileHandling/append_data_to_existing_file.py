# Python file program to append data to an existing file

open_file = open("writecontent.txt", "a") # Open file with append mode
append_data = open_file.write("Appended data")
open_file.close()