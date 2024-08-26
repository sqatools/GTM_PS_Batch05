#class
class ZXC:
    def __init__(self):
        print("initialize the object")
    def subtraction(self):
        num1 = 500
        num2 = 5
        print("subtaction:",num1-num2)

obj_var1 = ZXC()
obj_var1.subtraction()

print("_"*50)


#class
class school:
    #parametrize constuctor
    def __init__(self,school_name,school_location,school_fees,school_course):
        self.school_name = school_name
        self.school_location = school_location #instance variable
        self.school_fees = school_fees
        self.school_course = school_course
    def show_school_name(self):
        print("the school name is:",self.school_name)
    def show_school_locaion(self):
        print("the school locaion is:",self.school_location)
    def show_school_fees(self):
        print("the school fees is:",self.school_fees)
    def show_school_course(self):
        print("the course name is:",self.school_course)

    def show_school_details(self):
        print(self.school_name)
        self.school_location()
        self.school_fees()
        self.school_course()

school_obj = school("ssvm","bhubaneswar","10k","odia")
school_obj.show_school_name()
school_obj.show_school_details()

print("_"*50)



class school:
    #parametrize constuctor
    def __int__(self,school_name,school_location,school_fees,school_course = "english"):
        self.school_name = school_name
        self.school_location = school_location #instance variable
        self.school_fees = school_fees
        self.school_course = school_course
        self.school_teacher = "depeesh sir"
        self.show_greeting()

    def show_greeting(self):
        print(f"--------welcome to our {self.school_name}-----------")
    def show_school_name(self):
        print("the school name is:",self.school_name)
    def show_school_locaion(self):
        print("the school locaion is:",self.school_location)
    def show_school_fees(self):
        print("the school fees is:",self.school_fees)
    def show_school_course(self):
        print("the course name is:",self.school_course)

    def show_school_details(self):
        self.school_name()
        self.school_location()
        self.school_fees()
        self.school_course()

school_obj = school("ssvm","bhubaneswar","10k","odia")
school_obj.show_school_name()
school_obj.show_school_details()

print("_"*50)

school_obj2 = school("15k","english")
school_obj.show_school_details()

print("_"*50)

class school:

    #class variable
    school_country = "made in india"
    #parametrize constuctor
    def __int__(self,school_name,school_location,school_fees,school_course = "english"):
        self.school_name = school_name
        self.school_location = school_location #instance variable
        self.school_fees = school_fees
        self.school_course = school_course
        self.school_teacher = "depeesh sir"
        self.show_greeting()

    def show_greeting(self):
        print(f"--------welcome to our {self.school_name}-----------")
    def show_school_name(self):
        print("the school name is:",self.school_name)
    def show_school_locaion(self):
        print("the school locaion is:",self.school_location)
    def show_school_fees(self):
        print("the school fees is:",self.school_fees)
    def show_school_course(self):
        print("the course name is:",self.school_course)

    def show_school_details(self):
        self.school_name()
        self.school_location()
        self.school_fees()
        self.school_course()

    @classmethod
    def show_school_country_name(cls):
        print("school country name is:{cls.school.country}")



school_obj = school("ssvm","bhubaneswar","10k","odia")
school_obj.show_school_name()
school_obj.show_school_details()

print("_"*50)

school_obj2 = school("15k","english")
school_obj.show_school_details()
school_obj2.show_school_country_name()
























































