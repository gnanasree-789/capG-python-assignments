#Your task is to design an Employee Management System using Object-Oriented Programming (OOP) principles such as 
# abstraction, inheritance, and polymorphism in Python.

# Instructions:
# Create an Interface Employee (Abstract Base Class)

# Define an abstract class Employee using the ABC module.
# Include two abstract methods:
# work(self) -> str: Defines the work responsibilities of the employee.
# get_salary(self) -> float: Returns the salary of the employee.
# Implement Concrete Employee Classes

# Create two classes, Manager and Developer, that inherit from Employee.
# Each class should implement the work method to describe the employee’s role.
# Implement the get_salary method to return the salary of the employee.
# Create a Department Class to Manage Employees

# The Department class should store a list of employees.
# Implement methods:
# hire(self, employee: Employee): Adds an employee to the department.
# fire(self, employee: Employee): Removes an employee from the department.
# get_total_salary(self) -> float: Returns the total salary of all employees.
# show_employee_details(self): Displays all employees, their salary, and work description.
# Test the Implementation

# Create instances of Manager and Developer with names and salaries.
# Add them to a Department and display their details.
# Calculate and print the total salary expense.

from abc import ABC,abstractmethod
class EmployeeInterface(ABC):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @abstractmethod
    def work(self):
        pass
    @abstractmethod
    def get_salary(self):
        pass
class Manager(EmployeeInterface):
    def work(self):
        print(f"The role of the employee is Manager")
    def get_salary(self):
        return self.salary
class Developer(EmployeeInterface):
    def work(self):
        print(f"The role of the employee is Developer")
    def get_salary(self):
        return self.salary


class Department:
    def __init__(self):
        self.employees=[]
    def hire(self,employee):
        self.employees.append(employee)
        print(f"The employee is hired: {employee.name}")
    def fire(self,employee:EmployeeInterface):
        self.employees.remove(employee)
        print(f"The employee is Fired: {employee.name}")
    def get_total_salary(self):
         total=0
         for employee in self.employees:
            total += employee.get_salary()
         return total
    def show_employee_details(self):
        for employee in self.employees:
            print(f"Employee salary: {self.salary} work: {self.work()}")

manager1=Manager('gnani',2345)
manager2=Manager('sai',9876)
developer1=Developer('balu',76543)
developer2=Developer('nani',234)
department=Department()
department.hire(manager1)
department.hire(manager2)
department.hire(developer1)
department.hire(developer2)

department.show_employee_details()
print()
department.fire(manager2)
department.show_employee_details()
print()
department.get_total_salary()