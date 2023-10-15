'''
-> A super function is a built-in function that returns the object that represent the parent class
-> It allows to access the parent class's methods and attributes.
'''
# Creating Parent Class

class Person:
  def __init__(self, name, age) -> None:
    self.name = name
    self.age = age
  
  def display(self):
    print(self.name, self.age)
    
# Creating Child Class
class Student(Person):
  def __init__(self, name, age,dob):
    self.sName = name
    self.sAge = age
    self.dob = dob
    
    # Inherting the properties of the parent class
    super().__init__("Roman", age)
    
  def displayInfo(self):
    print(self.sName, self.sAge, self.dob)
    
    
sObj = Student("Test", 22, "29-03-2003")
sObj.display() # Roman 22
sObj.displayInfo()  # Test 22 29-03-2003
