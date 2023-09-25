# SYNTAX 
def function_name(parameters):
  """docstring"""
  '''statements'''
  
'''
 def ->           marks the start of the function header.
 function_name -> is the name of the function.
 parameters ->    are the values you pass into the function.
 """docstring""" ->  is a short description of the function's purpose (optional).
 statement(s) ->  are the actions to be executed.
'''

# # Simple function
def greet():
   print("Hello!")
  
greet()  # calling function

# Parameters & Arguments:
def greet(name):
   print(f"Hello {name}")
  
greet("Roman") # calling function


 # Return Statement
'''
 return statement allows a function to return a value.
'''

def add_numbers(num1, num2):
   num3 = num1 + num2
   return num3

#sum = add_numbers(5,5)
print(f"The sum of two number is {sum}") # Output: 10

# Using default arugument in the function

def my_func(name = "Roman Humagain"):
  print(f"Namaste {name} !")
  
my_func()

 # ==== QUESTONS ====
 
 # function to check whether a given number is odd or even
def check_number(num):
   if num % 2 == 0:
     return "Even"
   elif num % 2 != 0:
     return "Odd"
   else:
     return "Invalid Number"

num = int(input("Enter a integer value to check whether it is Even/Odd: "))
answer = check_number(num)
print(f"{num} is a {answer} number.")

# Function to take the two list and check if there any common element in the list then return True
def check_common(list1, list2):
  for i in list1:
    if i in list2:
      return True 
      break
    
    else:
      return False

list1 = []
list2 = []
for _ in range(1):
  for _ in range(5):
    num1 = int(input("Enter a elements for first list: "))  
    list1.append(num1)
  print()  
  for _ in range(5):
    num2 = int(input("Enter a elements for second list: "))  
    list2.append(num2)
  
print("All Done !!")
print

is_common = check_common(list1, list2)
print(f"{is_common}")