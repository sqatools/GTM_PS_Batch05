# Create a class structure for school institute

class school():

    def __init__(self, school_name, school_city, school_fees, school_subjects):
        self.s_name = school_name
        self.s_city = school_city
        self.s_fees = school_fees
        self.s_subjects = school_subjects

        print(f"School name is: {self.s_name}")
        print(f"School city is: {self.s_city}")

    def sch_fees(self):
        print("School fees is:", self.s_fees)

    def sch_subjects(self, val1, val2, val3, val4, val5):
        print("School subjects are:", self.s_subjects)

obj1 = school("Sacred Hearts", "Bangalore", "Rs.50000", ("Maths", "English", "Science", "Social", "Hindi"))
obj1.sch_fees()
obj1.sch_subjects("Maths", "English", "Science", "Social", "Hindi")
