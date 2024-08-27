
class Father:
    def __init__(self, fcar, fhome, fbusiness):
        self.f_car = fcar
        self.f_home = fhome
        self.f_business = fbusiness

    def show_fcar(self):
        print(f"Car name is: {self.f_car}")

    def show_fhome(self):
        print(f"{self.f_home}")

    def show_fbusiness(self):
        print(f"{self.f_business}")

class Son(Father):

    def __init__(self, sage, fcar, fhome, fbusiness):
        super().__init__(fcar, fhome, fbusiness)
        self.s_age = sage

    def show_sage(self):
        print(f"Son's age is: {self.s_age}")

    def show_all_details(self):
        self.show_sage()
        self.show_fcar()
        self.show_fhome()
        self.show_fbusiness()

obj = Son("24", "Mercedez", "Villa", "Car Company")
obj.show_all_details()

# Son's age is: 24
# Car name is: Mercedez
# Villa
# Car Company

