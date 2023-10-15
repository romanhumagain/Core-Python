'''
-> Inheritance allows us to define a class that inherits all the methods and properties from another class
-> Parent Class is the class being inherited from, also called the base class
-> Child Class is the class that inherits from another class, also called derived class
'''

# Creating a class named Person with firstname and lastname as the properties, ans a printname method

class Person:
  def __init__(self, first_name, last_name) -> None:
    self.first_name = first_name
    self.last_name = last_name
    
  def printname(self):
    print(self.first_name, self.last_name)
    
# Use the person class to create an object, and then execute the printname method
person_obj = Person("Roman", "Humagain")
person_obj.printname() # Roman Humagain

# Creating a clild class named Student that inherits the functionality from the another class
class Student(Person):
  def __init__(self, fname, lname, year):
    # To use the __init__ function from the super class
    super().__init__(fname, lname)
    
    # adding more properties for the Student class
    self.graduation_year = year
    
    
'''Now the student class has the same properties and method of the Person Class'''
student_obj = Student("Test", "User", 2026)
student_obj.printname() # Test User
print(student_obj.graduation_year)



# ==== WORKING WITH ANOTHER EXAMPLE ====
# creating class named Car

class Car:
  def __init__(self, windows, doors, engine_type):
    # Instance Variable
    self.windows = windows
    self.doors = doors
    self.engine_type = engine_type
    
  # Creating a method
  def driving(self):
    print("The car is used for driving")
    
# Creating a new class called Audi inheriting from the class Car
class Audi(Car):
  def __init__(self, windows, doors, engine_type, horsepower):
    # after using __init__ function in the child class, super() function is used to inheritate the feature of the Car class 
    super().__init__(windows, doors, engine_type)
    self.horsepower = horsepower
    
    
audiCr7 = Audi(4,6,"Diseal", 400)
print(audiCr7.engine_type)
print(audiCr7.horsepower)

# Calling the method from the parent class
audiCr7.driving()