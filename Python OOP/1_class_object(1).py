# Creating a class named Employee
'''
class Employee:
  pass

# creating a instance of the class Employee
emp_1 = Employee()

emp_1.name = "Roman Humagain"
emp_1.email = "romanhumagain@gmail.com"
emp_1.pay = 20000

print(emp_1.name)  # Roman Humagain'''

# Making above code more obtimized 

class Employee:
  
  def __init__(self, first_name, last_name, salary):
    # Instance Variable
    self.first_name = first_name
    self.last_name = last_name
    self.salary = salary
    self.email = first_name + "." + last_name + "@gmail.com"
    
  
  # Creating a method inside the class
  def display_fullname(self):
    return self.first_name + " " + self.last_name

# Creating instance for the class Employee
emp_inst1 = Employee("Roman", "Humagain", 20000)
emp_inst2 = Employee("Test", "User", 10000)

# Printing the email of the two instances
print(emp_inst1.email)
print(emp_inst2.email)

# To get the full name 
full_name = emp_inst1.display_fullname()
print(full_name)


