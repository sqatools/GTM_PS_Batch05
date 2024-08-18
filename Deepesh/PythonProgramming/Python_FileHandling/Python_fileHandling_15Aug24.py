"""
# Different file modes.
read mode (r) : Open file in read mode allow us to read all the data of the file.
write mode (w) : When open file in write mode and write some content in the file, it will
                 overwrite the existing content.
append mode (a) : When we open a file in append mode and write content in the file, then
                  it will append content at the end of the file.
"""
# write a python program to count the email id and phone number from given file.

def get_email_list_from_file(filename):
    email_list = []
    with open(filename, "r") as file:
        data = file.read()
        # get word list
        word_list = data.split(" ")
        print(word_list)
        # go through each word
        for word in word_list:
            # check word contains @
            if "@" in word and ".com" in word:
                # add word in email list
                email_list.append(word)
            else:
                continue

        print("email list :", email_list)


#get_email_list_from_file("test_email_read.txt")


def get_phone_numbers_list_from_file(filename):
    phone_list = []
    with open(filename, "r") as file:
        data = file.read()
        # get word list
        word_list = data.split(" ")
        print(word_list)
        # go through each word
        for word in word_list:
            # check word length is 10 and it contains only numbers
           if len(word) == 10 and word.isnumeric():
               phone_list.append(word)
           elif len(word) == 13 and "+91" in word:
               phone_list.append(word)

        print("phone list :", phone_list)

#get_phone_numbers_list_from_file("test_email_read.txt")


# write a file handling program to update the specific word in the file

def update_word_in_file(filename, word1, word2):
    with open(filename, "r") as file:
        file_data = file.read()
        print(file_data)

        print("_"*80)
        updated_data = file_data.replace(word1, word2)
        print(updated_data)

    with open(filename, "w") as file:
        file.write(updated_data)

#update_word_in_file("update_file_read.txt", "JAVA", "PYTHON")
update_word_in_file("update_file_read.txt", "PYTHON", "C++")
