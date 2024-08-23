"""
class: class in the blueprint of the object where we defined all the method/attribute and
       properties of the object.
object: Object is an entity through we can access all the properties/attribute/methods of the
        class.
methods: Method is a code block in side the class which has its own feature and functionality.
         There are three types of methods in the class
         1). Instance method/object method : Any method that we defined with first parameter as
             self, then that method is known as instance method.

         2). Class method : The method which interact with class variable, then it is known as class method.
         3). Static method :  The method which does not interact with class variable. or instance
                              variables. and static method is associated class name, and
                              no need to create the object of the class.

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



variables: There are two type of variable in the class
           1). Instance variable : The variable which we declare with self, then it is known as
           instance variable.

           2) Class  variable : The class variable we declare on class level.

self : self is nothing but the object of the class being,
       that help to access all methods and variables.
       -> when ever we call any method with obj, then the same object is first parameter in
          method to provide reference to the self.
"""


################## class with parametrize constructor ##############

class Car:
    # class variable
    car_country = "Made in India"

    # parametrize constructor
    def __init__(self, car_name, car_price, car_comp='Maruti'):
        self.Car_Name = car_name  # instance variable
        self.Car_Price = car_price  # instance variable
        self.Car_Company = car_comp  # instance variable
        self.Car_mialege = "20km/l"
        # self.show_greeting()
        # print(f"The car price is: {self.Car_Price}")

    # instance/object method
    def show_greeting(self):
        print(f"---- Welcome to the {self.Car_Company} -----")

    # instance/object method
    def show_car_name(self):
        print("The car name is :", self.Car_Name)

    # instance/object method
    def show_car_price(self):
        print("The car price is :", self.Car_Price)

    def show_car_company(self):
        print("Car company name is :", self.Car_Company)

    def show_car_details(self):
        self.show_car_name()
        self.show_car_price()
        self.show_car_company()
        print("Car mialege is :", self.Car_mialege)

    @classmethod
    def show_car_country_name(cls):
        """
        The method which interact with class variable, then it is known as class method.
        :return:
        """
        print(f"Car country name is : {cls.car_country}")

    @staticmethod
    def get_factorials(num):
        fact = 1
        for i in range(num, 0, -1):
            fact = fact*i

        print("Factorial; values:", fact)

#car_obj2 = Car("Grand Vitara", "15 lac")
#car_obj2.show_car_details()

#car_obj2.show_greeting()

#Car.show_greeting()


# car_obj2.show_car_country_name()

# Home work :
# create a class structor for school institude.

#Car.get_factorials(6) # 720


class XYZ:
    def __init__(abc, msg):
        abc.print_msg = msg

    def print_greeting_to_family(abc):
        print(abc.print_msg)

b1 = XYZ("Good morning to dear family")
b1.print_greeting_to_family()
