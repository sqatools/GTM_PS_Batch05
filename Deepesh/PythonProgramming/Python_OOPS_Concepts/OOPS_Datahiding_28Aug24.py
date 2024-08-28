"""
In Python data hiding can be achieved with the help of single underscore (_) or double underscore
 (__) as prefix for any variable or method name

1. if we define any variable or method name with single underscore or double underscore
   as prefix then those variables/methods will show in suggestion list

2. Still you want to access the hidden data then the variable/methods with single underscore
   is accessible without any issue.

3. If you want to access the variable/methods with double underscore then we have to user
   specific rule e.g. _<class_name>__variable/method
"""


class Company:
    def __init__(self, comp_name, comp_address, comp_domain):
        self.comp_name = comp_name
        self._company_add = comp_address
        self.__company_domain = comp_domain

    def show_company(self):
        print(f"The company name is: {self.comp_name}")

    def _show_company_address(self):
        print(f"The company address is: {self._company_add}")

    def __show_company_domain(self):
        print(f"Company work in this domain: {self.__company_domain}")

if __name__ == '__main__':
    obj = Company("TATA Motor", "Pune", "Passenger Vehicle")
    # we can easily access the single underscore method/variables
    obj._show_company_address()
    # to access the method/variable with double underscore , then we
    # to define the method and variable with class name _classname__variable/method name
    obj._Company__show_company_domain()
