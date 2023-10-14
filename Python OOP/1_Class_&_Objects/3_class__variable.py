class Employee:
  num_of_emps = 0
  raise_amount = 1.04
  
  def __init__(self, first_name, last_name, salary):
    
    # Instance Variable
    self.first_name = first_name
    self.last_name = last_name
    self.salary = salary
    self.email = first_name + "." + last_name + "@gmail.com"
    
    # to increase the number of the employees after creating a new instance of the Employee
    Employee.num_of_emps += 1
    
  
  # Creating a method inside the class
  def display_fullname(self):
    return self.first_name + " " + self.last_name

  def apply_raise(self):
    self.salary = int(self.salary * self.raise_amount)

emp1 = Employee("roman", "humagain", 20000)
emp2 = Employee("test", "user", 40000)

print(f"Salary before applying for increasing: {emp1.salary}")

# applying for salary increment
emp1.apply_raise() 

print(f"Salary after applying for increasing: {emp1.salary}")

print(f"The number of employee are {Employee.num_of_emps}")

print(emp1.raise_amount)  # 1.04

Employee.raise_amount =  3 
print(emp1.raise_amount) # 3 

