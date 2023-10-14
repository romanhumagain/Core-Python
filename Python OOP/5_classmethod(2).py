class Employee:
  num_of_emps = 0
  raise_amount_by = 1.04
  
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
    self.salary = int(self.salary * self.raise_amount_by)
    
  # creating classmethods to set the raise amount
  @classmethod
  def raise_amount(cls, amount):
    cls.raise_amount_by = amount
    
    
  @classmethod
  def from_string(cls, info):
    first_name, last_name, salary = info.split("-")
    return cls(first_name, last_name, salary)

emp_obj = Employee("Roman", "Humagain", 20000)
print(emp_obj.raise_amount_by)

Employee.raise_amount(7)
print(emp_obj.raise_amount_by)

emp_str1 = "Roman-Humagain-70000"
emp_str2 = "Anup-Poudel-40000"
emp_str3 = "Bijen-Shrestha-30000"

emp_obj1 = Employee.from_string(emp_str1)
print(emp_obj1.first_name)
print(emp_obj1.email)

emp_obj2 = Employee.from_string(emp_str2)
print(emp_obj2.first_name)
print(emp_obj2.email)







