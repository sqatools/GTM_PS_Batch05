# Program to get all the email ids from a text file

email_list = []
open_file = open("read_test_file","r")
get_email = open_file.read()

word_list = get_email.split(" ")

for word in word_list:
    if "@" in word:
        email_list.append(word)
    else:
        continue

print(email_list)
open_file.close()