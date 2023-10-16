'''
-> Method Overloading deals with the multiple methods in the same class with same name but different parameters

'''

class Calculator:
  def add(self, num1, num2):
    return num1 + num2
  
  def add(self, num1, num2, num3):
    return num1 + num2 + num3
  
  
# Creating an instane of the class Calculator
calc_obj = Calculator()

print(calc_obj.add(2,4))  # TypeError: Calculator.add() missing 1 required positional argument: 'num3'
print(calc_obj.add(2,4,4))  # 10


    