'''
-> Defined using `@classmethods` decorators
-> The first parameter passed to the class method is a reference to the class ('cls') itself, rather than an instance of a class
'''

# Basics Example for the classmethod

class People:
  total_num_of_people = 0
  
  def __init__(self, name):
    self.name = name 
    
    People.total_num_of_people += 1
    
  @classmethod
  def display_people(cls):
    return cls.total_num_of_people
    
    
# creating an instance of the class People
p1 = People("Roman")
p2 = People("Test User")

print(People.display_people())  # 2

  