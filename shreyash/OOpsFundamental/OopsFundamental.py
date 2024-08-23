###1
#class ABC:
#    def greeting(self):
#        print("Good Morning")

#obj_var = ABC()
#obj_var.greeting()

##2
#class ABC:
#    def addition(self):
#        num1= 30
#        num2= 40
#        print("Addition:",num1 + num2)
#obj_var= ABC()
#obj_var.addition()

##3: Default constructor
#class ABC:
#    def __init__(self):
#        print("Initialize the object")
#    def addition(self):
#        num1 = 300
#        num2 = 400
#        print("addition:",num1 + num2)
#obj_var= ABC()
#obj_var.addition()

##4:
#class Car:
#    def __init__(self, car_name, car_price, car_comp):
#        self.Car_Name = car_name
#        self.Car_price = car_price
#        self.Car_company = car_comp
##    def show_car_name(self):
##        print("The car name is:", self.Car_Name)
 #   def show_car_price(self):
#        print("The car price is:", self.Car_price)
#    def show_car_company(self):
#        print("The car company is:", self.Car_company)
#    def show_car_details(self):
#        self.show_car_name()
#        self.show_car_price()
#        self.show_car_company()
#car_obj = Car("Urus","4.5Cr","Lambo")
#car_obj.show_car_price()
#car_obj.show_car_details()

##Structure of school institute:

class school:
    def __init__(self, school_name, school_fee, school_course):
        self.School_Name = school_name
        self.School_Fee = school_fee
        self.School_Course = school_course
        self.show_greeting()
    def show_greeting(self):
        print(f"------Welcome to the {self.School_Name}-------")
    def show_school_name(self):
        print("The school name is:",self.School_Name)
    def show_school_fee(self):
        print("The school fee is:",self.School_Fee)
    def show_school_course(self):
        print("The school course is:",self.School_Course)

    def show_school_details(self):
        self.show_school_name()
        self.show_school_fee()
        self.show_school_course()

school_obj = school("GrowTechMind","18000","Python with Selenium")
school_obj.show_school_name()

school_obj.show_school_details()

####################################################
##Method 2####
class school:
    def __init__(self, school_name, school_fee, school_course):
        self.School_Name = "GrowTechMinds"
        self.School_Fee = "18000"
        self.School_Course = "Python WIth Selenium"
    def show_school_name(self):
        print("The school name is:",self.School_Name)
    def show_school_fee(self):
        print("The school fee is:",self.School_Fee)
    def show_school_course(self):
        print("The school course is:",self.School_Course)

    def show_school_details(self):
        self.show_school_name()
        self.show_school_fee()
        self.show_school_course()

#school_obj = school("GrowTechMind","18000","Python with Selenium")
school_obj.show_school_name()

school_obj.show_school_details()
