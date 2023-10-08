'''
-> the try block lets you to test a block of code for errors.
-> the excepts block lets you handle the error.
-> the else block lets you to execute code when there is no error.
-> the finally block lets you execute code, regardless of the result of try and excepts blocks
'''

# EXAMPLE

try:
  print(x)
except NameError:
  print("Variable x is not defined")   # Variable x is not defined
except:
  print("An exceptions occured ! ")

# Example for the else statement

try:
  print("Python is fun !!")
except Exception as error:
  print(error)
else:
  print("Program compiled without errors !")
  

# Use of finally
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


# Using raise keywords
x = "hello"
if not type(x) is int:
  raise TypeError("Only integer are allowed !! ")