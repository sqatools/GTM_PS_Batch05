"""
polymorphism means one particular person is doing multiple task.
method overriding : When two class connected via inheritance and both the classes have
                    same method name, but different behavior, so the child class method
                    will override the parent class method, and child class method will get
                    priority to call.

method overloading : When one class have two methods with same name but different parameters,
                    then that concept is known as method overloading.

                    Note : Python does not support method overloading. when we two methods
                    with same name in python class, then latest defined method will get priority.

Operator overloading : When one single operator is doing multiple task, then it is known as
                     operator overloading. e.g Plus(+) operator can add two int value, two string values
                    and two list as well.





"""



class Father:
    def __init__(self, fname, fbusiness, fcar, fhome):
        self.father_name = fname
        self.father_business = fbusiness
        self.father_car = fcar
        self.father_house = fhome

    def show_fname(self):
        print(f"The father name is: {self.father_name}")

    def show_fbusiness(self):
        print(f"Father business is: {self.father_business}")

    def show_fcar(self):
        print(f"Father is owning a car: {self.father_car}")

    def show_fhouse(self):
        print(f"Father is owning a house: {self.father_house}")

    def family_greeting(self):
        print("Hare krishna")


class Son(Father):
    def __init__(self, sname, fname, fbusiness, fcar, fhome):
        super().__init__(fname, fbusiness, fcar, fhome)
        self.son_name = sname

    def show_son_name(self):
        print(f"The son name is: {self.son_name}")

    def show_family_details(self):
        self.show_fname()
        self.show_fbusiness()
        self.show_fcar()
        self.show_fhouse()
        self.show_son_name()


    def family_greeting(self):
        print("Good Morning")

    def addition(self, n1, n2):
        print("addition of two numbers :", n1+n2)

    def addition(self, x1, x2, x3):
        print("addition of there numbers :", x1+x2+x3)



obj = Son("Rahul", "Rameshwar", "Construction", "BMW", "Bangalow")
obj.family_greeting()
obj.addition(30, 40, 50)



print("_"*50)
n1 = 40
n2 = 50
print("addition :", n1+n2)
print("addition :", n1.__add__(n2))
print(dir(int))


print("_"*50)
s1 = 'Hello'
s2 = 'Good Morning'
print("add string :", s1+s2)
print("Add string :", s1.__add__(s2))
print(dir(str))

print("_"*50)
l1= [3, 5, 7]
l2 = [4, 7, 8]
print("add two list :", l1+l2)
print("add two list :", l1.__add__(l2))
print(dir(list))
