# Convert all uppercase to lowercase in a word

word = input("Enter the word: ")
for char in word:
    if char.isupper():
        print(char.lower(), end="")
    else:
        print(char, end="")