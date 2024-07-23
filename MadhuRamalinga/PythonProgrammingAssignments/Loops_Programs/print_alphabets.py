# Print all alphabets from a-z and A-Z
print("Alphabets from a-z are: ")
for i in range(26):
    print(chr(97+i), end=" ")

print("")
print("")

print("Alphabets from A-Z are: ")
for j in range(26):
    print(chr(65+j), end=" ")

###################################### OR ##########################################

print("")
print("_"*50)

import string
print("Alphabet from a-z:")
for letter in string.ascii_lowercase:
    print(letter, end =" ")

print("")

print("\nAlphabet from A-Z:")
for letter in string.ascii_uppercase:
    print(letter, end =" ")