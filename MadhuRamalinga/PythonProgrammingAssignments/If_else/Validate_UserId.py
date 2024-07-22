# Python program to validate user_id in the list of user_ids.

id_list = [1,2,3,4,5]
id = int(input("Enter the ID: "))
if id in id_list:
    print("Valid ID")
else:
    print("Invalid ID")