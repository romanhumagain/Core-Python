# ==== EXAMPLE FOR THE MULTIPLE INHERITANCE ====
'''
suppose we have two base classes -'Flyer' for the character that can fly and
Swimmer class for the characterists that can swim
'''

class Flyer:
  def fly(self):
    print("I can fly easily !!")
  
class Swimmer:
  def swim(self):
    print("I can swim easily !!")

# Creating a derived class
'''
Consider a character named "Dragon" that can fly and swim. This character will inherit from both Flyer and Swimmer
'''

class Dragon(Flyer, Swimmer):
  def roar(self):
    print("Roar!")
    
draco = Dragon()
draco.fly()
draco.swim()
draco.roar()


# === WORKING WITH SOME OTHER EXAMPLE ====
# creating a base class named Car and Boat, each with thier own attributes set in the __init__ method

class Car:
  def __init__(self, make, model, wheels = 4):
    self.make = make
    self.model = model
    self.wheels = wheels
    
  def display(self):
    print(f"This is a {self.make} {self.model} car with {self.wheels} wheels.")

class Boat:
  def __init__(self, boat_type):
    self.boat_type = boat_type
    
  def display(self):
    print(f"This is a {self.boat_type} boat.")
    
    
# Creating a Derived Class
''' The AmphibiousCar class should be able to initialize attributes of both `Car` and `Boat` '''

class AmphibiousCar(Car, Boat):
  def __init__(self, make, model, boat_type):
    Car.__init__(self, make, model) # initializing Car attributes
    Boat.__init__(self, boat_type)  # initializing Boat attributes
  
  def display(self):
    Car.display(self)
    Boat.display(self)
    
    
# Utilizing the derived class
vehicle = AmphibiousCar("Toyota", "AmphibiousModel", "speedboat")
vehicle.display()

# Outputs:
'''
This is a Toyota AmphibiousModel car with 4 wheels.
This is a speedboat boat.
'''


# ==== MultiLevel Inheritance Example ====
'''
-> When we have a child and grandchild relationship. 
'''

class Base:
  def __init__(self, name):
    self.name = name
    
  def getName(self):
    return self.name
  
# Inherited Class
class Child(Base):
  def __init__(self, name, age):
    self.age = age
    super().__init__(name)
    
  def getAge(self):
    return self.age
  
class GrandChild(Child):
  def __init__(self, name, age, address):
    self.address = address
    
    super().__init__(name, age)
    
  def getAddress(self):
    return self.address
  
# Driver Code
grandChildObj = GrandChild("Test", 90, "Kathmandu")
print(grandChildObj.getName(),
      grandChildObj.getAge(),
      grandChildObj.getAddress()
      )
  
  

