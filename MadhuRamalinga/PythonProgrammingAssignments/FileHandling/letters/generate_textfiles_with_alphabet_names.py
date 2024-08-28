# Program to generate text files with all alphabets names

import string, os # Import os,string library

# Check if the files with the alphabet names exists or not
if not os.path.exists(""): # If not then make a new file
    os.makedirs("")

for letter in string.ascii_uppercase: # Iterate over letters in the alphabets
    with open(letter + ".txt", "w") as file: # Add corresponding letter to the file
        file.writelines(letter)