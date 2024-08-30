class Company:
    def __init__(self,comp_name,comp_address,comp_domain):
        self.Comp_Name = comp_name
        self._Comp_Add = comp_address
        self.__Comp_domain = comp_domain

    def show_company(self):
        print(f"the company name is:{self.Comp_Name}")
    def _show_company_address(self):
        print(f"the company address is:{self._Comp_Add}")
    def __show_company_domain(self):
        print(f"the caompany domain is:{self.__Comp_domain}")

if __name__ == '__main__':

    obj= Company("TATA MOTORS","Pune","Commercial Vehicles")

    obj.show_company()
    obj._show_company_address()
    obj._Company__show_company_domain()
