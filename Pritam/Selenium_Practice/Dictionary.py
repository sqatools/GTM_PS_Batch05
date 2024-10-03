# Create a dictionary
# my_dict = {"name":"Alice","age":30,"city":"new york"}
# print(my_dict)
# Add or update an entry
# my_dict["email"] = "alice@gmail.com"
# my_dict["age"] = 31
# print(my_dict)
# # Delete an entry
# del my_dict["city"]
# print(my_dict)

# # Merge two dictionaries
# dict1 = {"name":"Alice","age":30}
# dict2 = {"city": "New york","email":"abc@gmail.com"}
# merged_dict = {**dict1,**dict2}
# print(merged_dict)
# # Convert list to dictionary
# keys = ["name","age","city"]
# values = ["Alice",30,"new york"]
# my_dict = dict(zip(keys,values))
# print(my_dict)

# # sort a dictionary  by key
# my_dict = {"a":20,"b":30,"c":5,"d":6,"e":15,"f":20}
# sorted_dict = dict(sorted(my_dict.items()))
# print(sorted_dict)

# Update dictionary by new dictionary
# dict1 = {"name":"alice"}
# dict2 = {"age":30}
# dict1.update(dict2)
# print(dict1)

# invert a dictionary
# my_dict = {"name":"Alice","age":30,"Live":"usa"}
# inverse_dict = {v:k for k,v in my_dict.items()}
# print(inverse_dict)

# Filter dictionary by keys
# my_dict = {"name":"Alice","age":30,"Country":"USA"}
# filtered_dict = {k:my_dict[k]for k in ["name","age"]}
# print(filtered_dict)