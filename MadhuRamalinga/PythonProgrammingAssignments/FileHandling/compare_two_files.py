# Python file program to compare two files

import difflib
with open('read_file1') as file1:
    file1_text = file1.readlines()
with open('read_file2') as file2:
    file2_text = file2.readlines()

for line in difflib.unified_diff(file1_text, file2_text, fromfile='file name', tofile='file.txt', lineterm=''):
    print(line)

# --- file name
# +++ file.txt
# @@ -1,5 +1,8 @@
# -Hello 9825632745
#
# -BangaloreOnline Class
#
# -9969854933 Good Morning
#
# -Python Programming
#
# -8856971236
#
# +Line1 : This is India
#
# +Line2 : This is America
#
# +Line3 : This is Canada
#
# +Line4 : This is Australia
#
# +Line5 : This is Africa
#
# +Line6 : This is Korea
#
# +Line7 : This is Germany
#
# +Line8 : This is China