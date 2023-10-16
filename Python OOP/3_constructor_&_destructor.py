'''
-> Desctructor are called when an object gets destroyed.
'''

class Employee:
  # Constructor
  def __init__(self):
    print("Emplyoee Created !!")\
      
  # Dectructor
  def __del__(self):
    print("Destructor Called ! Employee Deleted.")
    
# Calling the instance of the class Employee
emp_obj = Employee()
del emp_obj


# Python Program to illustrate the destructor

class Person:
   # Initializing
    def __init__(self):
        print('Person created')
  
    # Calling destructor
    def __del__(self):
        print("Destructor called")
        
        
def create_obj():
  print("Making Object !!....")
  obj = Person()
  print("Function End...")
  return obj

print("Calling create_obj() function!")
obj = create_obj()
print("Program End ! ")

# Output
'''
Calling Create_obj() function...
Making Object...
Employee created
function end...
Program End...
Destructor called
'''
  