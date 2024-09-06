# Program to create employee management system using python

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_details(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)

class EmployeeManagementApp:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def display_all_employees(self):
        for employee in self.employees:
            employee.display_details()

# Create an instance of the EmployeeManagementApp class
app = EmployeeManagementApp()

# Add employees to the application
employee1 = Employee(1, "Robert Yates", 50000)
employee2 = Employee(2, "Kelly Smith", 60000)
employee3 = Employee(3, "Michael Potter", 55000)

app.add_employee(employee1)
app.add_employee(employee2)
app.add_employee(employee3)

# Display all employees in the application
app.display_all_employees()

# Employee ID: 1
# Name: Robert Yates
# Salary: 50000
# Employee ID: 2
# Name: Kelly Smith
# Salary: 60000
# Employee ID: 3
# Name: Michael Potter
# Salary: 55000