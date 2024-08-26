import json

def read_json_file(filename):
    with open(filename, "r") as file:
        data = file.read()
        json_data = json.loads(data)
        #print(json_data, type(json_data))
        return json_data


# read_json_file("users_data.json")
# print("username : ", read_json_file("users_data.json")["username"])
# print("email : ", read_json_file("users_data.json")["email"])
# print("phone : ", read_json_file("users_data.json")["phone"])

# write content to json file

def write_content_to_json_file(filename, content: dict):
    # convert the dictionary data to str formate with json objects
    json_object_data = json.dumps(content)
    print(json_object_data)
    # open file with write mode
    with open(filename, "w") as file:
        file.write(json_object_data)


employee_details = {
    'emp_name' : 'John',
    "emp_emil" : "john@gmail.com",
    "emp_phone" : 88789798,
    'emp_salary' : 100000,
    "emp_city" : "Mumbai"
}
write_content_to_json_file("sample_data.json", employee_details)

login_data = read_json_file("users_data.json")
login_data["url"] = "https://www.google.co.in"
login_data["browser"] = "Chrome"

write_content_to_json_file("users_data.json", login_data)





