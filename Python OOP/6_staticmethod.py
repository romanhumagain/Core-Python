'''
-> A static method is a method that belongs to the class rather than an instance of the class
-> Defined using the `@staticmethod` decorator
-> Don't take any specific first parameter(neither `self` nor `cls` )
-> Can't access or modify instance-specific or class-specific data.
-> Behave like a regular function
'''

# Example of using the staticmethod

class MathOperations:
  
  @staticmethod
  def add(a, b):
    return a + b
  
  @staticmethod
  def multiply(a, b):
    return a * b
  
  @staticmethod
  def is_even(num):
    if num%2 == 0:
      return True
    return False
  
result1 = MathOperations.add(5, 3)       # Outputs: 8
print(result1)

result2 = MathOperations.multiply(5, 3)  # Outputs: 15
print(result1)

check = MathOperations.is_even(4)        # Outputs: True
print(check)
  

  