# ==== variable that are created outside of the function is global variable ====

newString = "Roman Humagain"

def myFunc():
  print(newString) # accessing the variable named newString inside function.
myFunc()


# ==== using the global keyboard inside of the function to make the variable global ====

def myNewFunc():
  global newGlobalVariable
  newGlobalVariable = "Python is Cool !!"
  
# should call the function to access the global variable inside the function
myNewFunc()

print("The value inside the newGlobalVariable is", newGlobalVariable)
