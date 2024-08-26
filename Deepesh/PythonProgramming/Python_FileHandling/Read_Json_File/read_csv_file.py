import csv

def read_csv_file(filename):
    with open(filename, "r") as file:
        csv_file = csv.reader(file)
        #print(csv_file)
        for line in csv_file:
            print(line)


read_csv_file("emp_details.csv")
"""
emp_name
 suresh
 mohan
 rahul
 rohit
 virat
"""

"""
['emp_id', ' emp_name', ' emp_salary', ' emp_address']
['emp_01', ' suresh', ' 30000', ' Pune']
['emp_02', ' mohan', ' 40000', ' Mumbai']
['emp_03', ' rahul', ' 50000', ' Bangalore']
['emp_04', ' rohit', ' 60000', ' Chennai']
['emp_05', ' virat', ' 70000', ' Kolkata']
"""
