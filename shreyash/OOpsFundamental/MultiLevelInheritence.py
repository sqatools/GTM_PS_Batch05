class GrandFather:
    def __init__(self,gfname,gf_property):
        self.Gf_Name = gfname
        self.Gf_Property = gf_property
    def show_gf_name(self):
        print(f"Grandfather name is:{self.Gf_Name}")
    def show_gf_property(self):
        print(f"Grandfather property is:{self.Gf_Property}")
 
class Father(GrandFather):
    def __init__(self, fname, fbusiness, fcar, fhouse,gfname,gf_property):
        super().__init__(gfname,gf_property)
        self.Father_name = fname
        self.Father_business = fbusiness
        self.Father_car = fcar
        self.Father_house = fhouse

    def show_fname(self):
        print(f"the fathere name is:{self.Father_name}")

    def show_fbusiness(self):
        print(f"the father business is:{self.Father_business}")

    def show_fcar(self):
        print(f"the father car is:{self.Father_car}")

    def show_fhouse(self):
        print(f"the father house is:{self.Father_house}")

class Son(Father):
    def __init__(self, sname,fname, fbusiness, fcar, fhouse,gfname,gf_property):
        super().__init__(fname, fbusiness, fcar, fhouse,gfname,gf_property)
        self.Son_name = sname

        def show_Son_name(self):
            print(f"the son name is:{self.Son_name}")

    def show_family_details(self):
        self.show_gf_name()
        self.show_gf_property()


        self.show_fname()
        self.show_fbusiness()
        self.show_fcar()
        self.show_fhouse()

obj=Son("Shreyas","Sunil","Farmer","Maruti800","Banglow","Balasaheb","Construction")
obj.show_family_details()
print("_"*50)
obj.show_fbusiness()
print("_"*50)
obj.show_gf_name()
obj.show_gf_property()


