
class Father:
    def __init__(self, fcar, fhome):
        self.f_car = fcar
        self.f_home = fhome

    def show_fcar(self):
        print(f"Car name is: {self.f_car}")

    def show_fhome(self):
        print(f"{self.f_home}")

class Mother:
    def __init__(self, mbusiness):
        self.m_business = mbusiness

    def show_mbusiness(self):
        print(f"{self.m_business}")

class Daughter(Mother, Father):
    def __init__(self, dage, mbusiness, fcar, fhome):
        super().__init__(self, dage, mbusiness, fcar, fhome)
        self.d_age = dage

    def show_dage(self):
        print(f"Age is: {self.d_age}")

    def show_all_details(self):
        self.show_dage()
        self.show_fcar()
        self.show_fhome()
        self.show_mbusiness()


obj = Daughter("24", "Car Company", "Mercedez", "Villa")
obj.show_all_details()
