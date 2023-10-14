'''
-> A class are the real world entity of objects
-> A class is a blueprint for creating objects.
-> An objects ia an instance of a class
'''

# Creating basic class
class MyClass:
   x = 5
   
# Creating an object of a class
obj = MyClass()

# accessing the variable inside class
print(obj.x)

# Working with __init__ Methods
'''
-> It is a special method called a constructor and is automatically called when an object of the class is created

'''

class Person:
  
  def __init__(self, name, age, college, course):
     self.name = name
     self.age = age
     self.college = college
     self.course = course
     
# Creating an object of Person class
person_obj =Person("Roman", 20,"PCPS College", "Software Engineering")
print(person_obj.name)  
print(person_obj.college)
print(person_obj.course)


# Creating a methods inside class \
class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age
     
  def greet(self):
    print(f"Hello {self.name}")
        
person_obj = Person("Roman", 20)
person_obj.greet()


# More Example ......
class BankAccount:
  # declaring and initializing class variable
  bank_name = "Kumari Bank"
  branch = "Kushadevi"
  
  # Creating constructor
  def __init__(self,account_number, balance ):
     self.account_number = account_number
     self.balance = balance
     
  # Creating methods
  def deposit(self, amount):
    self.balance += amount
    print(f"{amount} is deposited into Account {self.account_number}. And the new balance is {self.balance}")
    
  def withdraw(self, amount):
    if self.balance >= amount:
      self.balance -= amount
      print(f"{amount} is successfully withdrew from the {self.account_number}. And the new balance is {self.balance}")
    else:
      print("Sorry! Unsuffecient amount in your account.")
  
  def display_amount(self):
     print("Account: {}, Balance {}".format(self.account_number, self.balance))
     
     
# Creating an object of the class BankAccount
account_obj = BankAccount(555985656342626, 4000)
print(f"The name of the bank is {account_obj.bank_name} which is located at {account_obj.branch}")

account_obj.deposit(2000)
account_obj.withdraw(1000)

# To display the amount in the bank account
account_obj.display_amount()