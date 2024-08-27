
class Grandfather:
    def __init__(self, gage):
        self.gf_age = gage

    def g_age(self):
        print(f"Grandfather's age is: {self.gf_age}")

class Father(Grandfather):
    def __init__(self, fbusiness, gage):
        super().__init__(gage)
        self.f_business = fbusiness

    def fa_business(self):
        print(f"Father's business is : {self.f_business}")

class Son(Father):
    def __init__(self, shome, fbusiness, gage):
        super().__init__(fbusiness, gage="70")
        self.s_home = shome

    def son_home(self):
        print(f"Son lives in a {self.s_home}")

    def show_details(self):
        self.son_home()
        self.fa_business()
        self.g_age()

obj = Son("Apartment", "Car Company", "75")
obj.show_details()

# Son lives in a Apartment
# Father's business is : Car Company
# Grandfather's age is: 70