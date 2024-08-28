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


obj = Son("Rahul", "Rameshwar", "Construction", "BMW", "Bangalow")

# getter get value of any specific variable
print(obj.__getattribute__('son_name')) # Rahul

# setter can set the new value to any parameter.
obj.__setattr__("son_name", "Shriyansh")
print(obj.son_name)


