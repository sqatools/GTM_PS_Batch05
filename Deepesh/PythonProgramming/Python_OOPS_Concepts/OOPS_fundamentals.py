"""
class: class in the blueprint of the object where we defined all the method/attribute and
       properties of the object.
object: Object is an entity through we can access all the properties/attribute/methods of the
        class.
methods: Method is a code block in side the class which has its own feature and functionality.
constructor: The constructor which initialize the memory for the object of the class
             when ever we create an object of the class, then constructor will be executed first
             There are 2 types of constructor
             1). Default constructor : by default while creating the object of the class, the
                 default constructor will initialize without any parameter.
                 def __init__(self):
                    print("Initialize the object")

             2). Parametrize constructor: When we define any parameter to the constructor then it
                 becomes parametrize constructor
                   def __init__(self, car_name, car_price, car_comp):
                        self.Car_Name = car_name # instance variable
                        self.Car_Price = car_price # instance variable
                        self.Car_Company = car_comp # instance variable



variables:


"""
# class
"""
class ABC:

    def __init__(self):
        print("Initialize the object")

    # Method
    def greeting(self):
        print("Good Morning")

    def addition(self, num1, num2):
        #num1 = 200
        #num2 = 500
        print("Addition :", num1+num2)


#creating object
obj_var = ABC()
# access the method with class object
obj_var.greeting()
obj_var.addition(300, 400)

#str1 = "Hello"
#str1.upper()

print("_"*50)
obj_var1 = ABC()
obj_var1.addition(500, 700)
"""


################## class with parametrize constructor ##############

class Car:

    # parametrize constructor
    def __init__(self, car_name, car_price, car_comp='Maruti'):
        self.Car_Name = car_name # instance variable
        self.Car_Price = car_price # instance variable
        self.Car_Company = car_comp # instance variable
        self.Car_mialege = "20km/l"
        self.show_greeting()
        print(f"The car price is : {self.Car_Price}")

    def show_greeting(self):
        print(f"---- Welcome to the {self.Car_Company} -----")

    def show_car_name(self):
        print("The car name is :", self.Car_Name)

    def show_car_price(self):
        print("The car price is :",self.Car_Price)

    def show_car_company(self):
        print("Car company name is :", self.Car_Company)

    def show_car_details(self):
        self.show_car_name()
        self.show_car_price()
        self.show_car_company()
        print("Car mialege is :", self.Car_mialege)


car_obj = Car("Nexon", "12 Lac", "TATA")
car_obj.show_car_name()
car_obj.show_car_details()


print("_"*50)

car_obj2 = Car("Grand Vitara", "15 lac")
car_obj2.show_car_details()


# Home work :
# create a class structor for school institude.
