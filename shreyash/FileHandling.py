#Q1:ReadFile
#def read_file_data(filename):
##    file = open(filename,"r")
#    file_data = file.read()
#    print(file_data)
#read_file_data("data_file_read.txt")
#------------------------------------------------

#Q2:Write Mode

#def write_content_to_file(filename,content):
#    file = open(filename,"w")
#    file.write(content)
#    file.close()
#write_content_to_file("data_file_read.txt","company name prospecta software pvt ltd")  #case2
#-------------------------------------------------------------------------------------------------

#Q3:Write mode with append method with existing file:
#def append_content_to_file(filename,content):
#    file = open(filename,"a")
#    file.write(content)
#    file.close()
#content = "\n appending fresh content to file"   #case1 adding data in exsting file and get add at the last
#append_content_to_file("data_file_read.txt", content)
#-------------------------------------------------------------------------------------------------------------

#Q4:With context manager
#def read_content_with_context(filename):
#    with open(filename,"r") as file:
#        data = file.read()
#        print(data)
#        print("check file is closed inside context manager:",file.closed)

#    print("check file is closed outside context manager:",file.closed)
#--------------------------------------------------------------------------------------------------------------
#Q5:Read specific line

#def read_specific_lines(filename,line_no):
#    with open(filename,"r") as file:
#        data = file.readline()
#        print(data)
#read_specific_lines("data1_file_read.txt",55) #line no.1 will print
#--------------------------------------------------------------------------------------------------------------

#Q6:Read to N number of lines
#def read_specific_lines(filename,line_no):
#    with open(filename,"r")as file:
#        for _ in range(line_no):
#            data = file.readline()
#            print(data)
#read_specific_lines("data1_file_read.txt",5)
#---------------------------------------------------------------------------------------------------------------

#Q7:Read Number of characters
#def read_number_of_characters(filename,no_byte):
#    with open(filename,"r") as file:
#        data = file.read(no_byte)
#        print(data)

#read_number_of_characters("data1_file_read.txt",23)
#--------------------------------------------------------------------------------------------------------------

#Q8:List of lines
#def read_list_of_lines(filename):
#    with open(filename,"r") as file:
#        lines_list = file.readline()
#        print(lines_list)

#read_list_of_lines("data1_file_read.txt")-------------- doubt
#------------------------------------------------------------------------------------------------------------

#Q9:
#def read_list_of_lines(filename):
#    with open(filename,"r") as file:
#       lines_list = file.readlines()
#        print(lines_list)
#        return lines_list

#list_lines = read_list_of_lines("data1_file_read.txt")

#for i in range(-3,0,1):
#    print(list_lines[i])

#for j in range(3):
#    print(list_lines[j])

#read_list_of_lines("data1_file_read.txt")

