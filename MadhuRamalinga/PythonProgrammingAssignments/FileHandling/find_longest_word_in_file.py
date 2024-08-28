# Python file program to find the longest word in a file

# Create variables
max_word = ''
max_len = 0

with open('read_test_file', 'r') as file: # Read file with read mode
    file_data = file.read()
    word_list = file_data.split()  # Convert data into words
    
    for word in word_list:  # Iterate over words
        if len(word) > max_len:  # Check for word with maximum length
            max_len = len(word)
            max_word = word
        else:
            continue
print("Max length word:", max_word)
