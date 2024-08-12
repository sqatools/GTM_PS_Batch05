from pprint import pprint

school = {
    'teacher': {
        'math': [
                {'Name' : 'mohan', 'address' :  'Pune', 'email' : 'mohan@gmail.com'},
                {'Name' : 'rahul', 'address' :  'Mumbai', 'email' : 'rahul@gmail.com'},
        ],
        'english': [
                {'Name' : 'mohit', 'address' :  'Indore', 'email' : 'mohit@gmail.com'},
                {'Name' : 'raghu', 'address' :  'Chennai', 'email' : 'raghu@gmail.com'}
        ],
        'chemistry': [
                {'Name' : 'Aman', 'address' :  'Pune', 'email' : 'Aman@gmail.com'},
                {'Name' : 'subham', 'address' :  'Mumbai', 'email' : 'subham@gmail.com'}
        ],
        'physics' : [
                {'Name' : 'madhu', 'address' :  'Pune', 'email' : 'madhu@gmail.com'},
                {'Name' : 'shwetha', 'address' :  'Mumbai', 'email' : 'shwetha@gmail.com'}
        ]
    },
    'student': {
        '9th' : [
            {'st_id': '9th_st_01', 'name' : 'pooja', 'email' : 'pooja@gmail.com', 'phone' : 234567},
            {'st_id': '9th_st_02', 'name' : 'megha', 'email' : 'megha@gmail.com', 'phone' : 76576746}
        ],
        '10th' : [
            {'st_id': '10th_st_01', 'name' : 'rishi', 'email' : 'rishi@gmail.com', 'phone' : 65476534},
            {'st_id': '10th_st_02', 'name' : 'ashish', 'email' : 'ashish@gmail.com', 'phone' : 77775464}
        ],
        '11th' : [
            {'st_id': '11th_st_01', 'name' : 'amit', 'email' : 'amit@gmail.com', 'phone' : 76756756},
            {'st_id': '11th_st_02', 'name' : 'ashish', 'email' : 'amit@gmail.com', 'phone' : 98898956}
        ],
        '12th' : [
            {'st_id':  '12th_st_01', 'name' : 'anshul', 'email' : 'anshul@gmail.com', 'phone' : 3434534543},
            {'st_id': '12th_st_02', 'name' : 'ishu', 'email' : 'ishu@gmail.com', 'phone' : 1233432445},
            {'st_id': '12th_st_03', 'name' : 'rishi', 'email' : 'rishi@gmail.com', 'phone' : 54643435},
        ]
    }
}

#pprint(school['teacher']['math'][1]['email'])

# write a program to get specific student details with his name

st_name = 'rishi'
st_class = '12th'


# first loop go through the school dict
for k1, v1 in school.items():
    #print(k1)
    #pprint(v1)
    if k1 == 'student':
        for k2, v2 in v1.items():
            #print(k2, v2)
            if k2 == st_class:
                #print(k2, v2)
                for st_data in v2:
                     #print(st_data['name'])
                     if st_name == st_data['name']:
                         #print(st_data[])
                        for k3, v3 in st_data.items():
                            print(k3, " : ", v3)
    #         else:
    #             continue
    #

# write a python program to get teachers email id with their name

print("_"*50)
teach_subject = 'physics'
teach_name = 'madhu'

# first loop go through the school dict
for k1, v1 in school.items():
    #print(k1)
    #pprint(v1)
    if k1 == 'teacher':
        for k2, v2 in v1.items():
            #print(k2, v2)
            if k2 == teach_subject:
                #print(k2, v2)
                for teach_data in v2:
                     #print(st_data['name'])
                     if teach_name == teach_data['Name']:
                         #print(st_data[])
                        for k3, v3 in teach_data.items():
                            print(k3, " : ", v3)





