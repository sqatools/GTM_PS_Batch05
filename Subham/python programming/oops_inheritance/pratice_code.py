#single inheritance
class tenthstudent:
    def __init__(self,tenmname,tendress,tenschooltime,tenphysicsteacher,tenfees):
        self.tenth_mname=tenmname
        self.tenth_dresscode = tendress
        self.tenth_schooltime = tenschooltime
        self.tenth_physicsteachername = tenphysicsteacher
        self.tenth_fees = tenfees
    def show_tenmname(self):
        print(f"tenth monitor name is:{self.tenth_mname}")
    def show_tendress(self):
        print(f"tenth dress code is:{self.tenth_dresscode}")
    def show_tenschooltime(self):
        print(f"tenth school timeing is:{self.tenth_schooltime}")
    def show_tenphysicsteacher(self):
        print(f"tenth physics teacher name is:{self.tenth_physicsteachername}")
    def show_tenfees(self):
        print(f"tenth course fees is:{self.tenth_fees}")
class ninethstudent(tenthstudent):
    def __init__(self,ninemname,tenmname,tendress,tenschooltime,tenphysicsteacher,tenfees):
        super().__init__(tenmname,tendress,tenschooltime,tenphysicsteacher,tenfees)
        self.ninethstudentent_mname=ninemname

    def show_ninethstudent_mname(self):
        print(f"monitor name is: {self.ninethstudentent_mname}")

    def show_school_details(self):
        self.show_tenmname()
        self.show_tendress()
        self.show_tenschooltime()
        self.show_tenphysicsteacher()
        self.show_tenfees()

obj = ninethstudent("subham", "rahul", "bluewhite", "6clock", "deepeshsir", "1lak")
obj.show_school_details()























