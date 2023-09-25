'''
-> When we declare a variable inside a function,
these variables have local scope, i.e they cannot be used ouside of the function
'''
def my_func():
  local_variable = "Roman"
  return local_variable

# This local_variable cannot be used outside of the function
# print(local_variable)


'''
-> When we create a variable outside of the function,
   then this variables can be accessed both inside and outside of the function, which is global variable.
'''

global_variables = "Mr Roman Humagain"

def func():
  print(global_variables)
  
# calling a function
func() # Mr Roman Humagain


'''
non local variable is used in python nested function whose local scope is not defined,
This means that the variable can be neither local not global
'''

def outer():
  var_type = "Locals"
  
  def inner():
    nonlocal var_type 
    var_type = "non locals "
    print(f"inner, {var_type}")
  
  inner()
  print(f"outer, {var_type}")
  
outer()


 