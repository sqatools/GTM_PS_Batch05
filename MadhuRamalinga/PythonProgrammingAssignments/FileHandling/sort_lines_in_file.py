# Sort Lines of File with Python

with open('read_file1','r') as file:
    lines = file.readlines() # Read list of lines
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            if len(lines[i]) > len(lines[j]):
                temp = lines[i]
                lines[i] = lines[j]
                lines[j] = temp
            else:
                continue

# re-write all the line one by one to the file

with open('read_file1','w') as file:
    all_lines = ''.join(lines)
    file.write(all_lines)