# Book Class:
# Attributes:
# title,author,isbn ,copies (number of available copies)
# Methods:
# add_book(book): Adds a book to the library's collection.
# remove_book(isbn): Removes a book from the library based on its ISBN.
# find_book(isbn): Finds and returns a book based on its ISBN.
# display_books(): Prints the details of all books in the library.

library=[]
class Book:
    def __init__(self,title,author,isbn,copies):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.copies=copies
    def add_book(self):
        library.append(self)
    def remove_book(self,isbn):
        for book in library:
            if book.isbn==isbn:
                library.remove(book)
                print(f"Book with isbn {book.isbn} is removed from library")
            else:
                print(f"Book with isbn {book.isbn} is not found")
    def find_book(self,isbn):
        for book in library:
            if book.isbn==isbn:
                print(f"Book with isbn {book.isbn} is found in library")
            else:
                print(f"Book with isbn {book.isbn} is not found")
    def display_books(self):
        print("Books in library:")
        for book in library:
            print(f"Title: {book.title}, author: {book.author}, isbn: {book.isbn}, copies: {book.copies}")
b1=Book('xyz','ijk',345678,4)
b1.add_book()
b2=Book('abc','lmn',9876,3)
b2.add_book()
b3=Book('sto','pqr',1234,5)
b3.add_book()
b1.display_books()
b1.find_book(9876)
b1.remove_book(9876)
b1.display_books()




# 2) we're building a system to represent various types of employees in a company. 
# All employees have some common attributes (like name, age, and salary), but different types of employees might have specific behaviors or additional attributes
# (like managers having departments, and engineers having special skills).
# a) take input from the user about employee details minimum 3 employees in every department
# b) find who is the manager for give department
# c) how many employees working in that given department
# d) take input as skill how many engineers have that give skill 
# e) print total employee in every department
# f) print total employees in all departments

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def display(self):
        return super().display() + f", Department: {self.department} (Manager)"

class Engineer(Employee):
    def __init__(self, name, age, salary, department, special_skill):
        super().__init__(name, age, salary)
        self.department = department
        self.special_skill = special_skill

    def display(self):
        return super().display() + f", Department: {self.department}, Skill: {self.special_skill}"

class Company:
    def __init__(self):
        self.departments = {}

    def add_employee(self, employee):
        if employee.department not in self.departments:
            self.departments[employee.department] = []
        self.departments[employee.department].append(employee)

    def get_manager(self, department):
        for emp in self.departments.get(department, []):
            if isinstance(emp, Manager):
                return emp.name
        return "No manager found."

    def count_employees(self, department):
        return len(self.departments.get(department, []))

    def count_engineers_with_skill(self, skill):
        count = 0
        for employees in self.departments.values():
            for emp in employees:
                if isinstance(emp, Engineer) and emp.special_skill == skill:
                    count += 1
        return count

    def total_employees(self):
        return sum(len(emp) for emp in self.departments.values())

    def total_employees_per_department(self):
        return {dept: len(emp) for dept, emp in self.departments.items()}

company = Company()

departments_count = int(input("Enter number of departments: "))
for _ in range(departments_count):
    department = input("Enter department name: ")
    
    manager_name = input(f"Enter manager name for {department}: ")
    manager_age = int(input(f"Enter age for {manager_name}: "))
    manager_salary = float(input(f"Enter salary for {manager_name}: "))
    manager = Manager(manager_name, manager_age, manager_salary, department)
    company.add_employee(manager)
    
    for _ in range(3): 
        emp_type = input("Enter employee type (engineer/other): ")
        name = input("Enter employee name: ")
        age = int(input(f"Enter age for {name}: "))
        salary = float(input(f"Enter salary for {name}: "))
        
        if emp_type.lower() == "engineer":
            skill = input("Enter engineer's special skill: ")
            employee = Engineer(name, age, salary, department, skill)
        else:
            employee = Employee(name, age, salary)
        
        company.add_employee(employee)

dept = input("Enter department to find the manager: ")
print(f"Manager of {dept}: {company.get_manager(dept)}")

dept = input("Enter department to count employees: ")
print(f"Total employees in {dept}: {company.count_employees(dept)}")

skill = input("Enter skill to find engineers with that skill: ")
print(f"Number of engineers with skill '{skill}': {company.count_engineers_with_skill(skill)}")

print("Total employees per department:")
for dept, count in company.total_employees_per_department().items():
    print(f"{dept}: {count}")

print(f"Total employees in all departments: {company.total_employees()}")
