"""
Inheritance : When one class aquire the property of another class then it is known as Inheritance

1. Single Inheritance : Class A -> Class B
2. Multilevel Inheritance : Class A -> Class B -> Class C
3. Multiple Inheritance
4. Hybrid Inheritance
""";
class mother:
    def __init____(self, mname, mbusiness):
        self.mname = mname
        self.mbusiness = mbusiness

    def show_monther_details(self):
        print("The mother name is :", self.mname)
        print("The mother is owning a business :", self.mbusiness)


class Father():
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

# MRO (Method resolution order)
class Son(Father, mother):
    def __init__(self, sname, fanme, fbusiness, fcar, fhome):
       super().__init__(fanme, fbusiness, fcar, fhome)
       self.sname = sname

    def show_son_name(self):
        print(f"The son name is: {self.sname}")

    def show_family_details(self):
        self.show_fname()
        self.show_fbusiness()
        self.show_fcar()
        self.show_fhouse()
        self.show_son_name()



obj = Son("Rahul", "Rameshwar", "Construction", "BMW", "Bangalow")
obj.show_family_details()
print("_"*50)
obj.show_fbusiness()
#print("Gf Properties :", obj.gfproperty)
obj.show_family_details()


