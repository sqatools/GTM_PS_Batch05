# Program to get all mobile numbers from a file

file = open('read_file1')
data = file.read().split()
mob_num = []

for val in data:
    if val.isnumeric():
        if len(val) == 10:
            mob_num.append(val)
print("Mobile numbers in the read_file1:", mob_num) # Mobile numbers in the read_file1: ['9825632745', '9969854933', '8856971236']