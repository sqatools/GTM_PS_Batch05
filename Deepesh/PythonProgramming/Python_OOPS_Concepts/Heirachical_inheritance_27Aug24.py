"""
Inheritance : When one class aquire the property of another class then it is known as Inheritance

1. Single Inheritance : Class A -> Class B
2. Multilevel Inheritance : Class A -> Class B -> Class C
3. Multiple Inheritance ->
4. Hierarchical  Inheritance -> Class A - class B , class A -> Class C
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


class YoungerSon(Father):
    def __init__(self, sname, fname, fbusiness, fcar, fhome):
       super().__init__(fname, fbusiness, fcar, fhome)
       self.sname = sname

    def show_son_name(self):
        print(f"The son name is: {self.sname}")

    def show_family_details(self):
        self.show_fname()
        self.show_fbusiness()
        self.show_fcar()
        self.show_fhouse()
        self.show_son_name()



class ElderSon(Father):
    def __init__(self, sname, fname, fbusiness, fcar, fhome):
       super().__init__(fname, fbusiness, fcar, fhome)
       self.sname = sname

    def show_son_name(self):
        print(f"The son name is: {self.sname}")

    def show_family_details(self):
        self.show_fname()
        self.show_fbusiness()
        self.show_fcar()
        self.show_fhouse()
        self.show_son_name()


if __name__ == '__main__':
    obj1 = YoungerSon("Mohit", "Mohan", "ImportExport", "BMW", "Villa")
    obj1.show_family_details()
    print(obj1.__module__)
    print(__name__)

# print("_"*50)
# obj2 = ElderSon("Rahul", "Mohan", "ImportExport", "BMW", "Villa")
# obj2.show_family_details()

