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
    def __init__(self,school_name,school_location,school_fees,school_course = "english"):
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



#single inheritance
class tenthstudent:
    def __init__(self,tenmname,tendress,tenschooltime,tenphysicsteacher,tenfees):
        self.tenth_mname=tenmname
        self.tenth_dresscode = tendress
        self.tenth_schooltime = tenschooltime
        self.tenth_physicsteachername = tenphysicsteacher
        self.tenth_fees = tenfees
    def show_tenmname(self):
        print(f"tenth monitor name is:{self.tenth_mname}")
    def show_tendress(self):
        print(f"tenth dress code is:{self.tenth_dresscode}")
    def show_tenschooltime(self):
        print(f"tenth school timeing is:{self.tenth_schooltime}")
    def show_tenphysicsteacher(self):
        print(f"tenth physics teacher name is:{self.tenth_physicsteachername}")
    def show_tenfees(self):
        print(f"tenth course fees is:{self.tenth_fees}")
class ninethstudent(tenthstudent):
    def __init__(self,ninemname,tenmname,tendress,tenschooltime,tenphysicsteacher,tenfees):
        super().__init__(tenmname,tendress,tenschooltime,tenphysicsteacher,tenfees)
        self.ninethstudentent_mname=ninemname

    def show_ninethstudent_mname(self):
        print(f"monitor name is: {self.ninethstudentent_mname}")

    def show_school_details(self):
        self.show_tenmname()
        self.show_tendress()
        self.show_tenschooltime()
        self.show_tenphysicsteacher()
        self.show_tenfees()

obj = ninethstudent("subham", "rahul", "bluewhite", "6clock", "deepeshsir", "1lak")
obj.show_school_details()























































